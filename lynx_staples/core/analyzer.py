"""Main analysis orchestrator for consumer staples companies."""

from __future__ import annotations

import dataclasses
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Optional

from rich.console import Console

from lynx_staples.core.fetcher import fetch_company_profile, fetch_financial_statements, fetch_info
from lynx_staples.core.news import fetch_all_news
from lynx_staples.core.reports import download_top_filings, fetch_sec_filings
from lynx_staples.core.storage import get_cache_age_hours, has_cache, load_cached_report, save_analysis_report
from lynx_staples.core.ticker import resolve_identifier
from lynx_staples.metrics.calculator import (
    calc_efficiency, calc_growth, calc_intrinsic_value, calc_market_intelligence,
    calc_business_quality, calc_profitability, calc_share_structure, calc_solvency,
    calc_valuation,
)
from lynx_staples.models import (
    AnalysisReport, CompanyProfile, CompanyStage, CompanyTier, Segment,
    EfficiencyMetrics, Filing, FinancialStatement, GrowthMetrics,
    InsiderTransaction, IntrinsicValue, MarketIntelligence,
    BusinessQualityIndicators, NewsArticle,
    ProfitabilityMetrics, ShareStructure, SolvencyMetrics, ValuationMetrics,
    classify_segment, classify_jurisdiction, classify_stage, classify_tier,
)

from lynx_investor_core.sector_gate import SectorMismatchError, SectorValidator

console = Console(stderr=True)

# Sectors and industries that this tool is designed for.
# Yahoo Finance labels GICS "Consumer Staples" as "Consumer Defensive".
_ALLOWED_SECTORS = {"consumer defensive", "consumer staples"}
_ALLOWED_INDUSTRIES = {
    # Packaged food & meats
    "packaged foods", "confectioners", "farm products",
    "food distribution", "agricultural inputs",
    # Beverages
    "beverages - non-alcoholic", "beverages—non-alcoholic",
    "beverages - brewers", "beverages—brewers",
    "beverages - wineries & distilleries", "beverages—wineries & distilleries",
    # Tobacco
    "tobacco",
    # Household & personal products
    "household & personal products", "personal services",
    # Food retail & hypermarkets
    "grocery stores", "discount stores", "food retail",
    "hypermarkets & super centers",
    # Drug retail
    "pharmaceutical retailers",
    # Education-services that are sometimes mis-classified into staples (allow none)
}
# Description patterns specific to consumer-staples operators.
# Word-boundary matched to avoid false positives from generic business language.
_CONSUMER_DESCRIPTION_PATTERNS = [
    r"\bpackaged food", r"\bconsumer staples\b", r"\bconsumer defensive\b",
    r"\bdividend aristocrat", r"\bdividend king\b",
    r"\bgrocery", r"\bsupermarket", r"\bhypermarket\b", r"\bsuper ?center\b",
    r"\bwarehouse club\b", r"\bmembership warehouse\b",
    r"\bdrugstore\b", r"\bpharmacy chain\b", r"\bdrug retail",
    r"\bsoft drink", r"\bbottled water\b", r"\benergy drink",
    r"\bbrewery\b", r"\bbrewer\b", r"\bdistillery\b", r"\bdistiller\b",
    r"\bspirits\b", r"\bwinery\b", r"\bbeer\b",
    r"\btobacco\b", r"\bcigarette", r"\bnicotine\b",
    r"\bhousehold products?\b", r"\bcleaning products?\b", r"\blaundry detergent\b",
    r"\bpersonal care\b", r"\bcosmetics?\b", r"\bskin care\b", r"\bhair care\b",
    r"\boral care\b", r"\btoothpaste\b",
    r"\bagribusiness\b", r"\bgrain processor", r"\boilseed\b",
    r"\bmeat processor", r"\bpoultry processor",
    r"\bsnack food", r"\bcereal\b", r"\bdairy products?\b", r"\bconfection",
    r"\bpet food\b", r"\bbaby food\b",
]

_SCOPE_MSG = (
    "the scope of this tool.\n\n"
    "Lynx Consumer Staples Analysis is specialized exclusively for:\n"
    "  - Packaged food, confectionery, and pet/baby food\n"
    "  - Non-alcoholic and alcoholic beverages\n"
    "  - Tobacco\n"
    "  - Household and personal-care products\n"
    "  - Food retail and hypermarkets / warehouse clubs\n"
    "  - Drug retail / pharmacy chains\n"
    "  - Agribusiness and food processing\n\n"
    "For general fundamental analysis, use lynx-fundamental instead"
)

_VALIDATOR = SectorValidator.build(
    allowed_sectors=_ALLOWED_SECTORS,
    allowed_industries=_ALLOWED_INDUSTRIES,
    description_patterns=_CONSUMER_DESCRIPTION_PATTERNS,
    scope_description=_SCOPE_MSG,
    agent_name="lynx-investor-consumer-staples",
)


def _validate_sector(profile: CompanyProfile) -> None:
    """Raise SectorMismatchError if *profile* is outside the consumer staples scope."""
    _VALIDATOR.validate(profile)
ProgressCallback = Callable[[str, AnalysisReport], None]


def run_full_analysis(identifier: str, download_reports: bool = True, download_news: bool = True,
                      max_filings: int = 10, verbose: bool = False, refresh: bool = False) -> AnalysisReport:
    return run_progressive_analysis(identifier=identifier, download_reports=download_reports,
        download_news=download_news, max_filings=max_filings, verbose=verbose, refresh=refresh, on_progress=None)


def run_progressive_analysis(
    identifier: str, download_reports: bool = True, download_news: bool = True,
    max_filings: int = 10, verbose: bool = False, refresh: bool = False,
    on_progress: Optional[ProgressCallback] = None,
) -> AnalysisReport:
    def _notify(stage: str, report: AnalysisReport) -> None:
        if on_progress is not None:
            on_progress(stage, report)

    console.print(f"[bold cyan]Resolving identifier:[/] {identifier}")
    ticker, isin = resolve_identifier(identifier)
    console.print(f"[green]Ticker:[/] {ticker}" + (f"  [dim]ISIN: {isin}[/dim]" if isin else ""))

    if not refresh and has_cache(ticker):
        age = get_cache_age_hours(ticker)
        age_str = f"{age:.1f}h ago" if age is not None else "unknown age"
        console.print(f"[bold green]Using cached data[/] [dim](fetched {age_str})[/]")
        cached = load_cached_report(ticker)
        if cached:
            try:
                report = _dict_to_report(cached)
            except Exception as exc:
                console.print(f"[yellow]Cached data is corrupt ({exc}), re-fetching...[/]")
            else:
                if isin and report.profile.isin is None:
                    report.profile.isin = isin
                console.print(
                    f"[green]{report.profile.name}[/] -- "
                    f"{report.profile.tier.value}  {report.profile.stage.value}"
                )
                _notify("complete", report)
                return report

    if refresh:
        console.print("[yellow]Refreshing data from network...[/]")

    console.print("[cyan]Fetching company profile...[/]")
    info = fetch_info(ticker)
    profile = fetch_company_profile(ticker, info=info)
    profile.isin = isin

    if not profile.isin:
        try:
            import yfinance as yf
            fetched_isin = yf.Ticker(ticker).isin
            if fetched_isin and fetched_isin != "-":
                profile.isin = fetched_isin
        except Exception:
            pass

    tier = classify_tier(profile.market_cap)
    profile.tier = tier
    stage = classify_stage(profile.description, info.get("totalRevenue"), info)
    profile.stage = stage
    profile.primary_segment = classify_segment(profile.description, profile.industry)
    profile.jurisdiction_tier = classify_jurisdiction(profile.country, profile.description)
    if profile.country:
        profile.jurisdiction_country = profile.country

    console.print(
        f"[green]{profile.name}[/] -- {profile.sector or 'N/A'} / {profile.industry or 'N/A'}"
        f"  [bold][{_tier_color(tier)}]{tier.value}[/]"
        f"  [{_stage_color(stage)}]{stage.value}[/]"
    )

    # Validate sector — refuse to analyze companies outside consumer staples
    _validate_sector(profile)

    if profile.primary_segment.value != Segment.OTHER.value:
        console.print(f"[cyan]Primary Segment:[/] {profile.primary_segment.value}")
    console.print(f"[cyan]Market Exposure:[/] {profile.jurisdiction_tier.value}")

    report = AnalysisReport(profile=profile)
    _notify("profile", report)

    console.print("[cyan]Fetching financial statements...[/]")
    statements = fetch_financial_statements(ticker)
    console.print(f"[green]Retrieved {len(statements)} annual periods[/]")
    report.financials = statements
    _notify("financials", report)

    console.print("[cyan]Calculating metrics...[/]")
    report.valuation = calc_valuation(info, statements, tier, stage)
    _notify("valuation", report)
    report.profitability = calc_profitability(info, statements, tier, stage)
    _notify("profitability", report)
    report.solvency = calc_solvency(info, statements, tier, stage)
    _notify("solvency", report)
    report.growth = calc_growth(statements, tier, stage)
    _notify("growth", report)
    report.efficiency = calc_efficiency(info, statements, tier)
    report.share_structure = calc_share_structure(info, statements, report.growth, tier, stage)
    _notify("share_structure", report)
    report.business_quality = calc_business_quality(
        report.profitability, report.growth, report.solvency,
        report.share_structure, statements, info, tier, stage,
    )
    _notify("business_quality", report)
    report.intrinsic_value = calc_intrinsic_value(info, statements, report.growth, report.solvency, tier, stage)
    _notify("intrinsic_value", report)

    # Market intelligence (insider activity, analysts, short interest, technicals)
    console.print("[cyan]Gathering market intelligence...[/]")
    try:
        import yfinance as yf
        ticker_obj = yf.Ticker(ticker)
        report.market_intelligence = calc_market_intelligence(
            info, ticker_obj, report.solvency, report.share_structure,
            report.growth, tier, stage,
        )
        _notify("market_intelligence", report)
    except Exception as exc:
        console.print(f"[yellow]Market intelligence failed: {exc}[/]")

    _ticker, _max = ticker, max_filings
    with ThreadPoolExecutor(max_workers=2) as pool:
        filings_future = pool.submit(lambda: fetch_sec_filings(_ticker)) if download_reports else None
        news_future = pool.submit(lambda: fetch_all_news(_ticker, profile.name)) if download_news else None

        if download_reports:
            console.print("[cyan]Fetching SEC/SEDAR filings...[/]")
        if download_news:
            console.print("[cyan]Fetching news...[/]")

        if filings_future is not None:
            try:
                fl = filings_future.result()
                console.print(f"[green]Found {len(fl)} filings[/]")
                if fl:
                    console.print(f"[cyan]Downloading top {_max} filings...[/]")
                    download_top_filings(_ticker, fl, max_count=_max)
                report.filings = fl
                _notify("filings", report)
            except Exception as exc:
                console.print(f"[yellow]Filings fetch failed: {exc}[/]")
        if news_future is not None:
            try:
                nw = news_future.result()
                console.print(f"[green]Found {len(nw)} articles[/]")
                report.news = nw
                _notify("news", report)
            except Exception as exc:
                console.print(f"[yellow]News fetch failed: {exc}[/]")

    _notify("conclusion", report)

    console.print("[cyan]Saving analysis...[/]")
    path = save_analysis_report(ticker, _report_to_dict(report))
    console.print(f"[bold green]Analysis saved to:[/] {path}")
    _notify("complete", report)
    return report


def _report_to_dict(report: AnalysisReport) -> dict:
    def _dc(obj):
        if obj is None:
            return None
        if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
            return {k: _dc(v) for k, v in dataclasses.asdict(obj).items()}
        if isinstance(obj, list):
            return [_dc(i) for i in obj]
        return obj
    return _dc(report)


def _dict_to_report(d: dict) -> AnalysisReport:
    profile = _build_dc(CompanyProfile, d.get("profile", {}))
    profile.tier = _parse_tier(d.get("profile", {}).get("tier", ""))
    profile.stage = _parse_stage(d.get("profile", {}).get("stage", ""))

    def _maybe(cls, key):
        raw = d.get(key)
        return _build_dc(cls, raw) if raw is not None else None

    return AnalysisReport(
        profile=profile,
        valuation=_maybe(ValuationMetrics, "valuation"),
        profitability=_maybe(ProfitabilityMetrics, "profitability"),
        solvency=_maybe(SolvencyMetrics, "solvency"),
        growth=_maybe(GrowthMetrics, "growth"),
        efficiency=_maybe(EfficiencyMetrics, "efficiency"),
        business_quality=_maybe(BusinessQualityIndicators, "business_quality"),
        intrinsic_value=_maybe(IntrinsicValue, "intrinsic_value"),
        share_structure=_maybe(ShareStructure, "share_structure"),
        market_intelligence=_maybe(MarketIntelligence, "market_intelligence"),
        financials=[_build_dc(FinancialStatement, s) for s in d.get("financials", [])],
        filings=[_build_dc(Filing, f) for f in d.get("filings", [])],
        news=[_build_dc(NewsArticle, n) for n in d.get("news", [])],
        fetched_at=d.get("fetched_at", ""),
    )


def _build_dc(cls, data: dict):
    import dataclasses as dc
    field_names = {f.name for f in dc.fields(cls)}
    return cls(**{k: v for k, v in data.items() if k in field_names})


def _parse_tier(raw) -> CompanyTier:
    if isinstance(raw, CompanyTier):
        return raw
    for t in CompanyTier:
        if t.value == str(raw) or t.name == str(raw):
            return t
    return CompanyTier.NANO


def _parse_stage(raw) -> CompanyStage:
    if isinstance(raw, CompanyStage):
        return raw
    for s in CompanyStage:
        if s.value == str(raw) or s.name == str(raw):
            return s
    return CompanyStage.GRASSROOTS


def _tier_color(tier) -> str:
    return {CompanyTier.MEGA: "bold green", CompanyTier.LARGE: "green", CompanyTier.MID: "cyan",
            CompanyTier.SMALL: "yellow", CompanyTier.MICRO: "#ff8800", CompanyTier.NANO: "bold red"}.get(tier, "white")


def _stage_color(stage) -> str:
    return {CompanyStage.PRODUCER: "bold green", CompanyStage.ROYALTY: "bold green",
            CompanyStage.DEVELOPER: "cyan", CompanyStage.EXPLORER: "yellow",
            CompanyStage.GRASSROOTS: "#ff8800"}.get(stage, "white")
