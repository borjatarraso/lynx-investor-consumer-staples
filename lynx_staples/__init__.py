"""Lynx Consumer Staples — Fundamental analysis for consumer staples companies."""

from pathlib import Path

# Suite-level constants come from lynx-investor-core (shared across every agent).
from lynx_investor_core import (
    LICENSE_NAME,
    LICENSE_TEXT,
    LICENSE_URL,
    SUITE_LABEL,
    SUITE_NAME,
    SUITE_VERSION,
    __author__,
    __author_email__,
    __license__,
    __year__,
)
from lynx_investor_core import storage as _core_storage

# Initialize the shared storage layer with this agent's project root so
# data/ and data_test/ live beside *this* package.
_core_storage.set_base_dir(Path(__file__).resolve().parent.parent)

# ---------------------------------------------------------------------------
# Agent-specific identity
# ---------------------------------------------------------------------------

__version__ = "5.4"  # lynx-investor-consumer-staples version (independent of core)

APP_NAME = "Lynx Consumer Staples Analysis"
APP_SHORT_NAME = "Consumer Staples Analysis"
APP_TAGLINE = "Consumer Staples Fundamental Analysis"
APP_SCOPE = "consumer staples companies"
PROG_NAME = "lynx-staples"
PACKAGE_NAME = "lynx_staples"
USER_AGENT_PRODUCT = "LynxStaples"
NEWS_SECTOR_KEYWORD = "consumer staples stock"

TICKER_SUGGESTIONS = (
    "  - For US mega-cap CPG, try: PG, KO, PEP, CL, KMB, MDLZ, MO",
    "  - For packaged food, try: GIS, K, KHC, CPB, MKC, HSY, HRL, SJM",
    "  - For beverages, try: KO, PEP, MNST, KDP, STZ, BUD, DEO",
    "  - For tobacco, try: PM, MO, BTI",
    "  - For food retail / hypermarket, try: WMT, COST, KR, BJ",
    "  - You can also type the full company name: 'Procter & Gamble'",
)

DESCRIPTION = (
    "Fundamental analysis specialized for consumer staples companies — "
    "packaged food, non-alcoholic and alcoholic beverages, tobacco, "
    "household and personal-care products, food and drug retail, "
    "hypermarkets, and agribusiness. Evaluates defensive operators "
    "across all maturity stages from emerging staples brands to mature "
    "Dividend Aristocrats using staples-specific metrics: organic revenue "
    "growth, pricing power, gross margin resilience, dividend coverage, "
    "free-cash-flow conversion, brand strength, distribution moat, and "
    "private-label exposure.\n\n"
    "Part of the Lince Investor Suite."
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load_logo_ascii() -> str:
    """Load the ASCII logo from img/logo_ascii.txt."""
    from lynx_investor_core.logo import load_logo_ascii
    return load_logo_ascii(Path(__file__).resolve().parent)


def get_about_text() -> dict:
    """Return structured about information (uniform across agents)."""
    from lynx_investor_core.about import AgentMeta, build_about
    meta = AgentMeta(
        app_name=APP_NAME,
        short_name=APP_SHORT_NAME,
        tagline=APP_TAGLINE,
        package_name=PACKAGE_NAME,
        prog_name=PROG_NAME,
        version=__version__,
        description=DESCRIPTION,
        scope_description=APP_SCOPE,
    )
    return build_about(meta, logo_ascii=_load_logo_ascii())
