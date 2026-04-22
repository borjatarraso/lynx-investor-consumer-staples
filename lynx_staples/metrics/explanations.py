"""Metric explanations for Lynx Consumer Staples Analysis."""

from __future__ import annotations
from lynx_staples.models import MetricExplanation

METRIC_EXPLANATIONS: dict[str, MetricExplanation] = {}


def _add(key, full_name, description, why_used, formula, category):
    METRIC_EXPLANATIONS[key] = MetricExplanation(
        key=key, full_name=full_name, description=description,
        why_used=why_used, formula=formula, category=category,
    )


# Valuation
_add("pe_trailing", "Price-to-Earnings Ratio (TTM)",
     "Compares stock price to trailing 12-month earnings per share.",
     "Primary consumer-staples valuation metric. Mature CPG names trade in "
     "the 18-25x range; tobacco trades at 8-13x; warehouse clubs (COST) "
     "earn premium 30-50x multiples.",
     "P/E = Price / EPS (TTM)", "valuation")
_add("pe_forward", "Forward P/E",
     "Price divided by consensus forward earnings.",
     "Forward-looking comparable. Useful when current earnings are "
     "depressed by input-cost inflation that pricing has not yet caught up to.",
     "Forward P/E = Price / Forward EPS", "valuation")
_add("pb_ratio", "Price-to-Book Ratio",
     "Compares stock price to book value per share.",
     "Less informative for asset-light branded staples; more relevant for "
     "agribusiness and food retail with significant tangible assets.",
     "P/B = Price / Book Value per Share", "valuation")
_add("ps_ratio", "Price-to-Sales Ratio",
     "Compares stock price to revenue per share.",
     "Useful anchor for emerging staples brands and growth food/beverage "
     "names where margins are still scaling. <1x is cheap for mature "
     "retail; 3-6x for high-growth challenger brands.",
     "P/S = Market Cap / Revenue", "valuation")
_add("p_fcf", "Price-to-Free-Cash-Flow",
     "Compares market cap to free cash flow.",
     "Best valuation anchor for mature staples operators — harder to "
     "manipulate than EPS and aligns with the dividend-funding profile. "
     "Target <22x for healthy mature operators.",
     "P/FCF = Market Cap / Free Cash Flow", "valuation")
_add("ev_ebitda", "Enterprise Value / EBITDA",
     "Capital-structure-neutral valuation.",
     "Preferred cross-sector comp for consumer staples. Mature CPG: "
     "12-18x. Tobacco: 8-11x. Hypermarkets: 14-20x. Beverages (KO/PEP): "
     "16-22x.",
     "EV/EBITDA = (Market Cap + Debt - Cash) / EBITDA", "valuation")
_add("ev_revenue", "Enterprise Value / Revenue",
     "EV divided by trailing revenue.",
     "Useful for emerging staples names and cross-comparing CPG operators "
     "of similar margin profile. <1x is cheap; >3x requires strong "
     "margin or organic-growth profile.",
     "EV/Revenue = EV / Revenue", "valuation")
_add("peg_ratio", "PEG Ratio",
     "P/E adjusted by growth rate.",
     "PEG < 1 suggests undervaluation relative to growth. Less useful "
     "for slow-growth mature staples; more useful for emerging brands.",
     "PEG = P/E / Annual EPS Growth Rate", "valuation")
_add("dividend_yield", "Dividend Yield",
     "Annual dividend as percentage of price.",
     "Central staples valuation metric — many are Dividend Aristocrats / "
     "Kings. Mature CPG yields 2-4%; tobacco yields 5-9%; food retail 1.5-3%. "
     "Always check the payout ratio and FCF coverage.",
     "Yield = Annual Dividends / Price", "valuation")
_add("earnings_yield", "Earnings Yield",
     "Inverse of P/E ratio.",
     "Compare to treasury yields for a relative-attractiveness read. "
     "Defensive staples often trade at low single-digit earnings yields.",
     "Earnings Yield = EPS / Price", "valuation")
_add("ev_per_store", "EV per Store / Location",
     "Enterprise value per physical location (when disclosed).",
     "A per-unit valuation for food retail and hypermarket chains. "
     "Comparable across chains within the same sub-segment.",
     "EV / Store Count", "valuation")
_add("price_to_tangible_book", "Price / Tangible Book",
     "Price vs tangible book value per share.",
     "Useful for asset-heavy food retail and agribusiness; less relevant "
     "for branded CPG dominated by goodwill / intangibles.",
     "P/TBV = Price / (Equity - Intangibles) / Shares", "valuation")
_add("cash_to_market_cap", "Cash-to-Market-Cap Ratio",
     "How much of market cap is backed by cash.",
     "Mostly relevant for emerging staples brands. >20% can signal either "
     "hidden value or under-leveraged balance sheet.",
     "Cash / Market Cap = Total Cash / Market Capitalization", "valuation")

# Profitability
_add("roe", "Return on Equity",
     "Profit generated per dollar of equity.",
     "Target ROE > 15% for mature staples operators. Tobacco and "
     "asset-light brand owners often exceed 30% on minimal book equity.",
     "ROE = Net Income / Equity", "profitability")
_add("roa", "Return on Assets",
     "Profit per dollar of assets.",
     "ROA > 8% is strong for branded CPG. Capital-intensive food retail "
     "naturally has lower ROA (3-6%).",
     "ROA = Net Income / Total Assets", "profitability")
_add("roic", "Return on Invested Capital",
     "Return on all invested capital.",
     "THE core consumer-staples quality metric. ROIC > 15% suggests a "
     "durable competitive advantage (brand, distribution, scale).",
     "ROIC = NOPAT / Invested Capital", "profitability")
_add("gross_margin", "Gross Margin",
     "Revenue remaining after cost of goods sold.",
     "Proxy for pricing power and brand strength. Tobacco / spirits: >55%. "
     "Branded CPG: 38-50%. Packaged food: 30-40%. Hypermarket / food "
     "retail: 22-28%.",
     "Gross Margin = Gross Profit / Revenue", "profitability")
_add("operating_margin", "Operating Margin",
     "Revenue remaining after all operating expenses.",
     "Operating leverage indicator. Tobacco: >40%. Branded CPG: 18-25%. "
     "Packaged food: 12-18%. Food retail: 2-4% (razor-thin).",
     "Operating Margin = Operating Income / Revenue", "profitability")
_add("net_margin", "Net Profit Margin",
     "Revenue remaining as net profit.",
     "Bottom-line profitability after interest and tax.",
     "Net Margin = Net Income / Revenue", "profitability")
_add("fcf_margin", "Free Cash Flow Margin",
     "Revenue converted to free cash flow.",
     "Measures actual cash generation that funds dividends and buybacks. "
     ">12% is strong for branded staples; >25% for tobacco.",
     "FCF Margin = FCF / Revenue", "profitability")
_add("ebitda_margin", "EBITDA Margin",
     "Revenue remaining as EBITDA.",
     "Approximates operating cash flow. >18% is healthy for CPG; >35% "
     "for tobacco; <8% for grocery / hypermarket retail.",
     "EBITDA Margin = EBITDA / Revenue", "profitability")
_add("sga_pct_of_revenue", "SG&A as % of Revenue",
     "Selling, general, and administrative expense as a fraction of revenue.",
     "Marketing-intensity indicator for staples brands. Branded CPG runs "
     "20-28% SG&A (heavy on advertising); rising SG&A% with flat volume "
     "is a private-label-pressure signal.",
     "SG&A% = SG&A / Revenue", "profitability")
_add("store_contribution_margin", "Store Contribution Margin (proxy)",
     "Estimated store-level margin after variable store costs.",
     "Unit economics indicator for food retail and hypermarket operators. "
     "Healthy operators show 3-6% store-contribution margin before "
     "corporate overhead.",
     "(Gross Profit - Variable SG&A) / Revenue", "profitability")

# Solvency
_add("debt_to_equity", "Debt-to-Equity Ratio",
     "Debt financing vs equity financing.",
     "Consumer staples can carry meaningful leverage given predictable "
     "cash flow. Mature CPG often runs 0.8-2.0x; tobacco can exceed 2x "
     "while retaining investment grade.",
     "D/E = Total Debt / Equity", "solvency")
_add("debt_to_ebitda", "Debt-to-EBITDA",
     "Leverage ratio relative to operating cash flow.",
     "The primary leverage metric for staples operators. <2x is "
     "conservative, 2-3.5x normal for mature CPG, >4.5x stressed.",
     "Debt/EBITDA = Total Debt / EBITDA", "solvency")
_add("current_ratio", "Current Ratio",
     "Short-term asset coverage of liabilities.",
     "Food retail inventories skew this metric high; >1.0 is acceptable "
     "given fast inventory turns and trade payables financing.",
     "Current Ratio = Current Assets / Current Liabilities", "solvency")
_add("quick_ratio", "Quick Ratio",
     "Liquidity excluding inventory.",
     "Important sanity check for food retail where inventory can be "
     "perishable. Branded CPG typically runs quick ratios near 1.",
     "Quick Ratio = (Current Assets - Inventory) / Current Liabilities", "solvency")
_add("interest_coverage", "Interest Coverage",
     "Ability to pay interest from operating earnings.",
     "> 6x is comfortable for staples operators given dividend-funding "
     "needs. < 3x signals balance-sheet stress in a rising-rate environment.",
     "Interest Coverage = Operating Income / Interest Expense", "solvency")
_add("lease_adjusted_debt_ratio", "Lease-Adjusted Leverage",
     "Debt-to-EBITDAR after capitalizing operating leases (8x rent proxy).",
     "Critical for food retail, hypermarkets, and drug retail where "
     "off-balance-sheet store-lease commitments are large. Target <4x; "
     ">5x is stressed.",
     "(Debt + 8 × Rent) / (EBITDA + Rent)", "solvency")
_add("altman_z_score", "Altman Z-Score",
     "Bankruptcy probability predictor.",
     "Z > 2.99: Safe. 1.81-2.99: Grey zone. < 1.81: Distress risk. "
     "Apply cautiously to asset-light brand owners.",
     "Z = 1.2(WC/TA) + 1.4(RE/TA) + 3.3(EBIT/TA) + 0.6(MV/TL) + 1.0(Sales/TA)",
     "solvency")
_add("cash_burn_rate", "Cash Burn Rate",
     "Annual rate of cash consumption for pre-profit operators.",
     "Relevant only for emerging / early-stage staples brands.",
     "Cash Burn = Annual Operating Cash Flow (when negative)", "solvency")
_add("cash_runway_years", "Cash Runway",
     "Years of operation at current burn rate.",
     "< 1 year = imminent financing. > 2 years = comfortable. Target for "
     "emerging staples brands: 18+ months.",
     "Cash Runway = Total Cash / Annual Burn Rate", "solvency")
_add("debt_service_coverage", "Debt Service Coverage",
     "EBITDA coverage of interest expense.",
     "> 6x is comfortable for mature staples. Levered staples names "
     "(tobacco, food retail) should target > 8x given dividend payouts.",
     "DSCR = EBITDA / Interest Expense", "solvency")

# Growth
_add("revenue_growth_yoy", "Revenue Growth (YoY)",
     "Annual revenue change.",
     "Core organic-growth driver. For mature staples, 2-6% is healthy "
     "(volume + pricing); scaling brands should deliver >12%.",
     "Growth = (Rev_Current - Rev_Prior) / |Rev_Prior|", "growth")
_add("revenue_cagr_3y", "Revenue CAGR (3-Year)",
     "3-year compound revenue growth.",
     "Smooths near-term cyclicality. > 6% is strong for mature staples "
     "operators; > 12% for scaling brands.",
     "CAGR = (End/Start)^(1/3) - 1", "growth")
_add("earnings_growth_yoy", "Earnings Growth (YoY)",
     "Annual net income change.",
     "Should track or exceed revenue growth to validate operating "
     "leverage and pricing-power capture.",
     "Growth = (NI_Current - NI_Prior) / |NI_Prior|", "growth")
_add("capex_intensity", "CAPEX Intensity",
     "CAPEX as % of revenue.",
     "Asset intensity indicator. Asset-light brand owners: < 3%. "
     "Branded CPG: 3-5%. Food retail / hypermarket: 2-4%. "
     "Agribusiness / processing: 4-7%.",
     "CAPEX Intensity = CAPEX / Revenue", "growth")
_add("same_store_sales_proxy", "Organic Growth Proxy",
     "Revenue growth minus total-asset growth.",
     "When companies don't disclose organic growth directly, this proxy "
     "separates same-store / same-distribution growth from M&A and "
     "footprint expansion. Positive values suggest the existing base "
     "is producing more.",
     "Rev Growth - Asset Growth", "growth")
_add("shares_growth_yoy", "Share Dilution (YoY)",
     "Annual change in shares outstanding.",
     "Mature staples should run net buybacks. Net dilution > 2%/yr in a "
     "Dividend-Aristocrat-style operator signals capital-allocation issues.",
     "Dilution = (Shares_Current - Shares_Prior) / Shares_Prior", "growth")
_add("shares_growth_3y_cagr", "Dilution / Buyback CAGR (3-Year)",
     "3-year compound share dilution rate.",
     "Tracks capital-discipline trend. Best-in-class staples deliver "
     "-1% to -3% (net buyback) CAGR alongside the dividend.",
     "CAGR = (Shares_End / Shares_Start)^(1/3) - 1", "growth")
_add("operating_leverage", "Operating Leverage",
     "Earnings growth relative to revenue growth.",
     "> 1.5x signals scaling margin expansion; < 1x suggests margin "
     "compression from input-cost or trade-spend pressure.",
     "Op Leverage = Earnings Growth / Revenue Growth", "growth")

# Efficiency
_add("inventory_turnover", "Inventory Turnover",
     "How many times per year inventory is sold.",
     "Packaged food: 5-9x. Beverages: 8-12x. Food retail: 12-20x. "
     "Hypermarkets / Costco: 12-15x. Declining turnover is an early "
     "stress signal for retailers.",
     "Inventory Turnover = COGS / Average Inventory", "efficiency")
_add("days_inventory", "Days Inventory",
     "Average days required to sell inventory.",
     "Food retail: 20-35 days. Packaged food: 50-80 days. Tobacco: "
     "60-90 days. Declining days = healthier; rising days = potential "
     "trade-spend or shelf-velocity issues.",
     "Days Inventory = 365 / Inventory Turnover", "efficiency")
_add("working_capital_intensity", "Working-Capital Intensity",
     "Working capital as % of revenue.",
     "Costco famously runs negative working capital (favorable — paid "
     "by customers before paying suppliers). Branded CPG: 5-15%. Food "
     "retail: -2% to +5%.",
     "WC Intensity = Working Capital / Revenue", "efficiency")
_add("revenue_per_employee", "Revenue per Employee",
     "Top-line revenue divided by headcount.",
     "Labour-productivity proxy. Branded CPG: $400-700K. Food retail: "
     "$200-400K. Costco: $700K+. Tobacco: $1M+ on small workforces.",
     "Revenue / Full-Time Employees", "efficiency")

# Business quality
_add("quality_score", "Consumer Staples Business Quality Score",
     "Composite quality score (0-100).",
     "Evaluates brand strength, unit economics, financial position, "
     "management alignment, and capital discipline. >70 is high quality "
     "(Dividend-Aristocrat tier), <35 is weak.",
     "Weighted sum of brand strength, unit economics, financial position, "
     "insider alignment, dilution", "business_quality")
_add("brand_strength", "Brand Strength",
     "Qualitative assessment of pricing power.",
     "Derived primarily from gross margin level and trend. Premium staples "
     "brands sustain >50% gross margin with stable / expanding pricing.",
     "Inferred from Gross Margin level + trend", "business_quality")
_add("cyclical_sensitivity", "Defensive Sensitivity",
     "Inverse exposure to consumer-confidence and macro cycles.",
     "Tobacco and household / personal products are most defensive. "
     "Agribusiness and food retail carry moderate cycles tied to "
     "commodities and retailer pricing.",
     "Inferred from sub-segment classification", "business_quality")
_add("unit_economics_quality", "Unit Economics Quality",
     "Combined ROIC + operating margin assessment.",
     "Strong unit economics is the single most reliable long-term "
     "performance indicator for staples operators.",
     "Composite of ROIC and Operating Margin", "business_quality")
_add("channel_mix_quality", "Channel Mix Quality",
     "Qualitative read on asset-light brand vs capex-heavy retail.",
     "Asset-light brand owners produce higher ROIC and capital returns. "
     "Inferred from CAPEX intensity.",
     "Inferred from CAPEX / Revenue", "business_quality")


SECTION_EXPLANATIONS = {
    "profile": {
        "title": "Company Profile",
        "description": (
            "Company identification, market cap tier, operator maturity stage, "
            "primary consumer-staples sub-segment (packaged food, beverages, "
            "tobacco, household / personal products, food retail, etc.), and "
            "geographic market-exposure tier."
        ),
    },
    "valuation": {
        "title": "Valuation Metrics",
        "description": (
            "Price-based ratios. P/E, P/FCF and dividend yield are the primary "
            "anchors for mature staples operators; EV/EBITDA enables cross-"
            "comparison. For emerging brands, P/S and cash-to-market-cap are "
            "more useful."
        ),
    },
    "profitability": {
        "title": "Profitability Metrics",
        "description": (
            "Margin and return analysis. Gross margin is the proxy for pricing "
            "power; ROIC separates Dividend-Aristocrat-tier franchises from "
            "commodity-like operators. Includes SG&A% (advertising intensity) "
            "and a store-contribution proxy for retail formats."
        ),
    },
    "solvency": {
        "title": "Solvency & Survival",
        "description": (
            "Balance sheet strength. Debt/EBITDA and lease-adjusted leverage "
            "are the core metrics — operating-lease commitments are large for "
            "food retail, hypermarkets, and drug retail. Cash runway only "
            "matters for pre-profit emerging operators."
        ),
    },
    "growth": {
        "title": "Growth & Capital Discipline",
        "description": (
            "Revenue/earnings growth, CAPEX intensity, organic-growth proxy, "
            "and share dilution / buybacks. Mature staples should run net "
            "buybacks alongside the dividend; >2% dilution per year is a red "
            "flag in the sector."
        ),
    },
    "efficiency": {
        "title": "Operating Efficiency",
        "description": (
            "Asset turnover, inventory turnover, days inventory, working-"
            "capital intensity, and revenue per employee. Working-capital "
            "discipline is especially differentiating in food retail (Costco "
            "is the gold standard)."
        ),
    },
    "share_structure": {
        "title": "Share Structure",
        "description": (
            "Shares outstanding, fully diluted, insider ownership, and "
            "institutional holdings. Family-controlled staples names "
            "(Hershey Trust, Mars, Anheuser-Busch InBev) historically deliver "
            "long-term-oriented capital allocation."
        ),
    },
    "business_quality": {
        "title": "Consumer Staples Business Quality Assessment",
        "description": (
            "Staples-specific quality scoring. Evaluates brand strength, "
            "unit economics, financial position, management alignment, and "
            "capital discipline. Includes defensive-sensitivity tagging."
        ),
    },
    "intrinsic_value": {
        "title": "Intrinsic Value Estimates",
        "description": (
            "Multiple valuation methods adapted by stage. Mature operators: "
            "DCF + Dividend Discount Model + EV/EBITDA comps. Scaling "
            "operators: EV/EBITDA peer comps. Emerging: EV/Revenue with "
            "margin-ramp. Brand licensors: DCF on royalty stream."
        ),
    },
    "conclusion": {
        "title": "Assessment Conclusion",
        "description": (
            "Weighted scoring across 5 categories with weights adapted by both "
            "tier and operator stage. Includes a 10-point consumer-staples "
            "screening checklist."
        ),
    },
}


CONCLUSION_METHODOLOGY = {
    "overall": {
        "title": "Conclusion Methodology",
        "description": (
            "Score is a weighted average of 5 categories (valuation, "
            "profitability, solvency, growth, business quality). Weights vary "
            "by BOTH company tier AND operator stage. Mature defensive "
            "operators: profitability and quality weighted at 25% each. "
            "Emerging staples brands: solvency and growth weighted at 25-35%. "
            "Verdicts: Strong Buy (>=75), Buy (>=60), Hold (>=45), Caution "
            "(>=30), Avoid (<30)."
        ),
    },
    "valuation": {
        "title": "Valuation Score",
        "description": (
            "Starts at 50. Adjusted by P/E, P/FCF, EV/EBITDA, P/S, and P/B. "
            "Early-stage / emerging staples brands get a bonus for low P/B."
        ),
    },
    "profitability": {
        "title": "Profitability Score",
        "description": (
            "Starts at 50. ROIC is weighted most heavily, then gross margin, "
            "operating margin, and FCF conversion. Pre-profit operators "
            "default to 50 since margins are not meaningful yet."
        ),
    },
    "solvency": {
        "title": "Solvency Score",
        "description": (
            "Starts at 50. Debt/equity, debt/EBITDA, current ratio, interest "
            "coverage, and cash runway for pre-profit operators. Emerging "
            "staples brands are penalized heavily for any material debt."
        ),
    },
    "growth": {
        "title": "Growth Score",
        "description": (
            "Starts at 50. Revenue growth, 3-year CAGR, earnings growth, and "
            "share dilution. Scaling stage operators get the highest growth "
            "thresholds; net buybacks earn a bonus."
        ),
    },
    "business_quality": {
        "title": "Consumer Staples Business Quality Score",
        "description": (
            "Composite of brand strength / gross margin (25pts), unit "
            "economics / ROIC (25pts), financial position (20pts), "
            "management alignment (15pts), and capital discipline (15pts). "
            "Includes defensive-sensitivity tagging."
        ),
    },
}


def get_explanation(key): return METRIC_EXPLANATIONS.get(key)


def get_section_explanation(section): return SECTION_EXPLANATIONS.get(section)


def get_conclusion_explanation(category=None):
    return CONCLUSION_METHODOLOGY.get(category or "overall")


def list_metrics(category=None):
    metrics = list(METRIC_EXPLANATIONS.values())
    return [m for m in metrics if m.category == category] if category else metrics
