"""Consumer-staples-focused sector and industry insights."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SectorInsight:
    sector: str
    overview: str
    critical_metrics: list[str] = field(default_factory=list)
    key_risks: list[str] = field(default_factory=list)
    what_to_watch: list[str] = field(default_factory=list)
    typical_valuation: str = ""


@dataclass
class IndustryInsight:
    industry: str
    sector: str
    overview: str
    critical_metrics: list[str] = field(default_factory=list)
    key_risks: list[str] = field(default_factory=list)
    what_to_watch: list[str] = field(default_factory=list)
    typical_valuation: str = ""


_SECTORS: dict[str, SectorInsight] = {}
_INDUSTRIES: dict[str, IndustryInsight] = {}


def _add_sector(sector, overview, cm, kr, wtw, tv):
    _SECTORS[sector.lower()] = SectorInsight(
        sector=sector, overview=overview, critical_metrics=cm,
        key_risks=kr, what_to_watch=wtw, typical_valuation=tv,
    )


def _add_industry(industry, sector, overview, cm, kr, wtw, tv):
    _INDUSTRIES[industry.lower()] = IndustryInsight(
        industry=industry, sector=sector, overview=overview,
        critical_metrics=cm, key_risks=kr, what_to_watch=wtw,
        typical_valuation=tv,
    )


_add_sector(
    "Consumer Defensive",
    "Consumer staples companies sell goods that consumers buy regardless of "
    "economic conditions — food, beverages, tobacco, household and personal-"
    "care products, and groceries. Demand is inelastic, revenue is "
    "predictable, margins are defended by brand equity and distribution "
    "scale, and free cash flow is highly converted into dividends. Pricing "
    "power, organic growth, and private-label resilience distinguish "
    "Dividend-Aristocrat franchises from commodity-like operators.",
    ["Organic revenue growth (volume + price)", "Gross margin resilience",
     "Dividend yield & 5-year dividend growth", "FCF conversion (FCF / Net Income)",
     "ROIC", "Debt/EBITDA"],
    ["Input-cost inflation (commodities, packaging, energy)",
     "Private-label / store-brand encroachment",
     "Currency translation in international portfolios",
     "Weight-loss drugs (GLP-1) reducing snack / packaged-food demand",
     "Regulatory pressure (sugar tax, plain packaging, PFAS)",
     "Channel disruption (Amazon, Instacart) compressing retailer margins"],
    ["Consumer Price Index (food at home component)",
     "Volume vs price split of organic growth",
     "Private-label market share trends",
     "Commodity input prices (wheat, corn, sugar, dairy, aluminum)",
     "Dividend payout ratio and FCF coverage",
     "Distribution and shelf-space wins / losses"],
    "P/E 18-25x for mature CPG. EV/EBITDA 12-18x. Dividend yield 2-4% with "
    "low single-digit dividend growth. Tobacco trades at 8-13x P/E with "
    "5-9% yields. Hypermarkets earn 18-30x P/FCF on durable cash flow.",
)

_add_sector(
    "Consumer Staples",
    "Alias for Consumer Defensive — see the Consumer Defensive entry for detail.",
    ["Organic revenue growth", "Gross margin", "Dividend coverage",
     "FCF conversion", "ROIC", "Debt/EBITDA"],
    ["Input-cost inflation", "Private-label competition",
     "FX translation", "GLP-1 demand drag", "Regulatory pressure"],
    ["Food CPI", "Volume vs price", "Private-label share",
     "Commodity inputs", "Payout ratio"],
    "P/E 18-25x. EV/EBITDA 12-18x.",
)


_add_industry(
    "Packaged Foods", "Consumer Defensive",
    "Packaged-food companies (GIS, K, KHC, CPB, MDLZ, HSY, MKC, HRL, SJM) "
    "build brands around convenience, taste, and trusted nutrition. The "
    "best franchises hold #1 or #2 share in their categories and earn "
    "35-45% gross margins. Volume is structurally pressured by GLP-1 drugs "
    "and private-label substitution; pricing has carried growth in recent "
    "inflationary cycles.",
    ["Organic revenue growth (volume + price)",
     "Gross margin (target >35%)",
     "Operating margin (target >15%)",
     "ROIC", "Dividend payout ratio", "FCF conversion"],
    ["Input-cost inflation (grain, dairy, sugar, packaging)",
     "Private-label encroachment in core aisles",
     "GLP-1 drugs reducing snack / sugary-food consumption",
     "Retailer concentration (Walmart, Kroger pricing pressure)",
     "Activist pressure to break up portfolios",
     "Health & wellness shift away from processed food"],
    ["Volume vs price split of organic growth",
     "Private-label market share by category",
     "Net-input-cost inflation/deflation",
     "Innovation contribution to net sales (>5% is healthy)",
     "Distribution wins (new SKUs, foodservice expansion)"],
    "P/E 17-22x. EV/EBITDA 12-16x. P/FCF 18-25x. Dividend yield 2.5-4%.",
)

_add_industry(
    "Non-Alcoholic Beverages", "Consumer Defensive",
    "Soft drinks, bottled water, energy drinks, and coffee (KO, PEP, MNST, "
    "KDP, CELH) lead consumer staples on brand equity and distribution. "
    "Concentrate-and-bottler models (KO, PEP) generate 60%+ gross margins "
    "and 25-30% operating margins. Energy drinks have been the fastest-"
    "growing sub-category; carbonated soft drinks are flat-to-declining in "
    "developed markets, growing in emerging markets.",
    ["Organic volume growth", "Pricing / mix",
     "Gross margin (target >55%)", "Operating margin (target >25%)",
     "ROIC", "International growth %"],
    ["Sugar tax legislation and health regulation",
     "Plastic / packaging regulatory pressure",
     "Aluminum and PET resin input costs",
     "Bottler relationship economics",
     "Energy-drink competition (MNST vs CELH vs Red Bull)"],
    ["Global organic growth (volume + pricing)",
     "Energy-drink share gains",
     "Bottler system performance",
     "International (especially emerging markets) volume",
     "Innovation pipeline (zero-sugar, functional beverages)"],
    "Concentrate model (KO/PEP): P/E 22-28x, EV/EBITDA 16-22x. "
    "Energy drinks (MNST, CELH): P/E 25-40x. Dividend yield 2.5-3.5%.",
)

_add_industry(
    "Alcoholic Beverages", "Consumer Defensive",
    "Brewers, distillers, and vintners (BUD, STZ, DEO, BF.B, TAP) earn "
    "premium margins on brand heritage and category leadership. Spirits "
    "outperform beer in developed markets on premiumization; tequila is "
    "the fastest-growing sub-category. Wine is structurally challenged by "
    "shifting generational consumption.",
    ["Organic revenue growth", "Premiumization mix",
     "Gross margin (target >55% for spirits)",
     "Operating margin", "Brand portfolio depth", "Pricing power"],
    ["GLP-1 drugs reducing alcohol consumption",
     "Generational shift away from beer / wine",
     "Excise tax increases",
     "Tariffs on imported spirits",
     "Cannabis as substitution category"],
    ["Premium/super-premium mix shift",
     "Tequila and ready-to-drink growth",
     "On-premise vs off-premise channel split",
     "International growth (especially Asia for spirits)",
     "Innovation in non-alcoholic / low-alcohol"],
    "Spirits leaders (DEO, BF.B): P/E 22-30x, EV/EBITDA 16-22x. "
    "Brewers (BUD, TAP): P/E 14-20x, EV/EBITDA 9-13x. Yield 2-4%.",
)

_add_industry(
    "Tobacco", "Consumer Defensive",
    "Tobacco operators (PM, MO, BTI, IMBBY) earn the highest cash returns "
    "in consumer staples on inelastic demand and category-leading pricing "
    "power. Combustible cigarette volumes decline 3-5% per year; pricing "
    "more than offsets volume decline. Reduced-risk products (heat-not-"
    "burn, e-cigarettes, oral nicotine) drive long-term growth narratives. "
    "ESG screen-outs limit institutional ownership; high yields compensate.",
    ["Pricing power (price/mix > volume decline)",
     "Reduced-risk product (RRP) revenue growth",
     "Operating margin (target >40%)",
     "Dividend yield (typically 5-9%)",
     "FCF conversion", "ROIC"],
    ["Regulatory pressure (plain packaging, menthol bans, flavour bans)",
     "Excise tax increases reducing affordability",
     "Litigation (especially US)",
     "Reduced-risk product transition execution risk",
     "ESG screen-outs limiting valuation multiple",
     "Illicit / counterfeit cigarette trade"],
    ["RRP revenue % of total",
     "Combustible price elasticity",
     "Regulatory pipeline by major market",
     "FCF generation and dividend coverage",
     "International expansion of next-gen products"],
    "Tobacco: P/E 8-13x, EV/EBITDA 8-11x. Dividend yield 5-9%. "
    "Trades at structural discount due to ESG; high cash returns.",
)

_add_industry(
    "Household Products", "Consumer Defensive",
    "Household-products companies (PG, CL, CHD, CLX, RB.L) build trusted "
    "brands across cleaning, fabric care, hair care, and oral care. P&G "
    "is the gold standard with #1 or #2 share in nearly every category. "
    "50%+ gross margins reflect pricing power. Innovation cadence and "
    "advertising-to-sales ratio drive long-term share defence against "
    "private label.",
    ["Organic revenue growth (volume + price/mix)",
     "Gross margin (target >45%)",
     "Operating margin (target >20%)",
     "ROIC (target >15%)", "Dividend coverage", "Innovation contribution %"],
    ["Private-label encroachment in commodity categories",
     "Input-cost inflation (oleochemicals, pulp, packaging)",
     "Currency translation (large international exposure)",
     "Retailer pricing pressure",
     "Category disruption from DTC challengers (Dollar Shave, Native)"],
    ["Volume vs price split of organic growth",
     "Brand share trends in core categories",
     "Innovation as % of sales",
     "Pricing actions and consumer pushback",
     "Marketing spend as % of revenue (10-12% is healthy)"],
    "Household products: P/E 22-28x, EV/EBITDA 15-19x. "
    "Dividend yield 2-3% with 5-7% dividend growth. P&G is the benchmark.",
)

_add_industry(
    "Personal Products", "Consumer Defensive",
    "Personal-care companies (EL, KMB, COTY, NWL) span beauty, skincare, "
    "fragrance, hygiene, and oral care. Beauty (EL, prestige skincare) "
    "trades on Chinese consumer health and travel-retail recovery. Mass "
    "personal care (KMB, COTY) operates closer to packaged-food economics. "
    "Premium beauty earns 70%+ gross margins; mass personal care 35-45%.",
    ["Organic revenue growth", "Gross margin",
     "Operating margin", "China revenue %",
     "Premium / mass mix", "Travel-retail performance"],
    ["Chinese consumer slowdown (especially prestige beauty)",
     "Travel-retail downturn",
     "Influencer / DTC brand competition",
     "Currency translation",
     "Counterfeit / grey-market leakage"],
    ["China same-store sales / Hainan duty-free",
     "Travel-retail recovery (especially Asia)",
     "Skincare vs makeup mix",
     "DTC and Sephora channel growth",
     "New product launch performance"],
    "Prestige beauty (EL): P/E 22-35x in normalized environments. "
    "Mass personal care (KMB): P/E 18-22x, yield 3-4%.",
)

_add_industry(
    "Food Retail", "Consumer Defensive",
    "Grocery retailers (KR, ACI, AD.AS, WMK) operate on razor-thin 1-3% "
    "operating margins and depend on volume, private-label penetration, "
    "and cost discipline. Fresh and prepared-food growth, fuel rewards, "
    "and pharmacy attachment are key differentiators. Online grocery "
    "remains structurally unprofitable for most operators.",
    ["Identical / comparable-store sales",
     "Gross margin (target 22-28%)",
     "Operating margin (target 2-4%)",
     "Inventory turnover", "Private-label penetration",
     "Digital sales mix"],
    ["Walmart and Costco pricing pressure",
     "Amazon / Whole Foods grocery expansion",
     "Labour inflation (unionized workforce)",
     "Online grocery cost-to-serve",
     "Food deflation cycles compressing margins"],
    ["ID-store sales (excluding fuel)",
     "Inflation / deflation in food at home",
     "Private-label growth",
     "Digital sales (pickup + delivery)",
     "Pharmacy and fuel contribution"],
    "Food retail: P/E 12-18x, EV/EBITDA 6-9x. Yield 1.5-3%. "
    "Thin margins make small swings in comp sales meaningful.",
)

_add_industry(
    "Hypermarkets & Super Centers", "Consumer Defensive",
    "Hypermarkets and warehouse clubs (WMT, COST, BJ) combine grocery and "
    "general merchandise at scale. Costco's membership model produces "
    "industry-leading customer loyalty (>90% renewal) and 8-10% operating "
    "margins on the membership fee alone. Walmart has built a credible "
    "Amazon-competitor in e-commerce and advertising. These names are "
    "often the highest-quality defensive operators in the sector.",
    ["Comparable-store sales (ex-fuel)",
     "Membership fee income (clubs)",
     "Renewal rate (target >88% for clubs)",
     "Operating margin", "E-commerce growth",
     "Advertising / 3P revenue"],
    ["Membership-fee adoption ceiling",
     "Wage and labour inflation",
     "Tariff exposure (especially WMT)",
     "Online grocery cost-to-serve",
     "Amazon competition in non-grocery"],
    ["Comp sales (ex-fuel, ex-FX)",
     "Renewal rate trends",
     "Membership fee per member growth",
     "E-commerce penetration (>15% is best-in-class)",
     "Advertising and Marketplace revenue growth"],
    "COST: P/E 35-50x reflecting durable cash flow. "
    "WMT: P/E 25-32x. Yield 0.5-1.5% — re-rated as quality compounders.",
)

_add_industry(
    "Drug Retail", "Consumer Defensive",
    "Drug retailers (WBA, CVS-retail, Boots) face structural pressure as "
    "PBM and payer dynamics compress pharmacy reimbursements while "
    "front-of-store competes against e-commerce. CVS has integrated as a "
    "vertical PBM-insurer-pharmacy. Walgreens has struggled with capital "
    "discipline and store-closure cycles. Pharmacy-script growth is a key "
    "metric.",
    ["Comparable-pharmacy script growth",
     "Front-of-store comp sales",
     "Pharmacy gross margin",
     "Total operating margin", "Store productivity"],
    ["PBM reimbursement cuts",
     "Mail-order and Amazon pharmacy competition",
     "Front-of-store erosion to e-commerce",
     "Opioid litigation overhang",
     "Workforce shortages in pharmacist staffing"],
    ["Pharmacy script growth",
     "Generic dispensing rate",
     "Front-of-store comp",
     "Store rationalization progress",
     "Capital allocation (dividend, buybacks)"],
    "Drug retail: P/E 8-14x reflecting structural concerns. "
    "Yield often 4-6%. Highly sensitive to PBM pricing dynamics.",
)

_add_industry(
    "Agribusiness", "Consumer Defensive",
    "Agribusiness operators (ADM, BG, TSN, CTVA) process and trade "
    "agricultural commodities. Earnings are inherently more volatile than "
    "branded staples, with margin compression / expansion driven by crop "
    "spreads, ethanol economics, and protein demand. ESG transition (plant-"
    "based protein, biofuels mandates) reshapes long-term opportunity sets.",
    ["Crush margins (oilseed processing)",
     "Origination volumes",
     "Operating margin trend", "ROIC across the cycle",
     "FCF conversion"],
    ["Commodity-price cycles (corn, soybeans, wheat)",
     "Crush margin compression",
     "Trade and tariff disruption (US-China grain flows)",
     "Climate and weather shocks",
     "Biofuels policy reversal"],
    ["South American crush margins",
     "Ethanol crush spread",
     "Renewable diesel / biofuel policy",
     "China soybean imports",
     "Protein demand and meat-processing margins"],
    "Agribusiness: P/E 10-16x, EV/EBITDA 6-10x. Cyclical earnings make "
    "trailing multiples misleading. Yield 2-3%.",
)


def get_sector_insight(sector: str | None) -> SectorInsight | None:
    return _SECTORS.get(sector.lower()) if sector else None


def get_industry_insight(industry: str | None) -> IndustryInsight | None:
    return _INDUSTRIES.get(industry.lower()) if industry else None


def list_sectors() -> list[str]:
    return sorted(s.sector for s in _SECTORS.values())


def list_industries() -> list[str]:
    return sorted(i.industry for i in _INDUSTRIES.values())
