# Lynx Consumer Staples Analysis

> Fundamental analysis specialized for consumer staples companies — packaged food, beverages, tobacco, household and personal-care products, food and drug retail, hypermarkets, and agribusiness.

Part of the **Lince Investor Suite**.

## Overview

Lynx Consumer Staples is a comprehensive fundamental analysis tool built specifically for consumer-staples investors. It evaluates defensive operators across all maturity stages — from emerging direct-to-consumer challenger brands to mature Dividend Aristocrats — using staples-specific metrics, stage-aware valuation methods, and defensive-sensitivity assessments.

### Key Features

- **Stage-Aware Analysis**: Automatically classifies operators as Early Stage / Pre-Profit, Emerging Staples Brand, Scaling Staples Operator, Mature Defensive Operator, or Brand Licensor / Asset-Light — and adapts all metrics and scoring accordingly
- **Staples-Specific Metrics**: Gross margin trend, organic-growth proxy (revenue minus asset growth), inventory turnover, lease-adjusted leverage, SG&A leverage, store-contribution proxy, dividend coverage, and capex intensity
- **4-Level Relevance System**: Marks each metric as Critical, Relevant, Contextual, or Irrelevant based on the operator's maturity stage
- **Market Intelligence**: Insider transactions, institutional holders, analyst consensus, short interest, price technicals with golden/death cross detection, and XLP / sub-segment ETF comparisons
- **10-Point Consumer Staples Screening Checklist**: Evaluates margin quality, ROIC, leverage, growth, dilution, insider ownership, FCF generation, and valuation discipline
- **Defensive Sensitivity Tagging**: Flags tobacco / household / packaged food as inelastic; agribusiness and food retail as more cyclical
- **Sub-Segment Detection**: Automatically identifies primary staples segment (Packaged Food, Non-Alcoholic Beverages, Alcoholic Beverages, Tobacco, Household Products, Personal Care, Food Retail, Hypermarket, Drug Retail, Agribusiness)
- **Multiple Interface Modes**: Console CLI, Interactive REPL, Textual TUI, Tkinter GUI
- **Export**: TXT, HTML, and PDF report generation
- **Sector & Industry Insights**: Deep context for Packaged Foods, Non-Alcoholic Beverages, Alcoholic Beverages, Tobacco, Household Products, Personal Products, Food Retail, Hypermarkets & Super Centers, Drug Retail, and Agribusiness

### Target Companies

Designed for analyzing companies like:
- **Packaged Food**: GIS, K, KHC, CPB, MDLZ, MKC, HSY, HRL, SJM, CAG
- **Non-Alcoholic Beverages**: KO, PEP, MNST, KDP, CELH
- **Alcoholic Beverages**: BUD, STZ, DEO, BF.B, TAP
- **Tobacco**: PM, MO, BTI, IMBBY
- **Household Products**: PG, CL, CHD, CLX, RB.L
- **Personal Care**: EL, KMB, COTY, NWL
- **Food Retail / Grocery**: KR, ACI, AD.AS, WMK
- **Hypermarkets / Warehouse Clubs**: WMT, COST, BJ
- **Drug Retail**: WBA, CVS
- **Agribusiness**: ADM, BG, TSN, CTVA

## Installation

```bash
# Clone the repository
git clone https://github.com/borjatarraso/lynx-investor-consumer-staples.git
cd lynx-investor-consumer-staples

# Install in editable mode (creates the `lynx-staples` command)
pip install -e .
```

### Dependencies

| Package        | Purpose                              |
|----------------|--------------------------------------|
| yfinance       | Financial data from Yahoo Finance    |
| requests       | HTTP calls (OpenFIGI, EDGAR, etc.)   |
| beautifulsoup4 | HTML parsing for SEC filings         |
| rich           | Terminal tables and formatting       |
| textual        | Full-screen TUI framework            |
| feedparser     | News RSS feed parsing                |
| pandas         | Data analysis                        |
| numpy          | Numerical computing                  |

All dependencies are installed automatically via `pip install -e .`.

## Usage

### Direct Execution
```bash
# Via the runner script
./lynx-investor-consumer-staples.py -p PG

# Via Python
python3 lynx-investor-consumer-staples.py -p KO

# Via pip-installed command
lynx-staples -p MO
```

### Execution Modes

| Flag | Mode | Description |
|------|------|-------------|
| `-p` | Production | Uses `data/` for persistent cache |
| `-t` | Testing | Uses `data_test/` (isolated, always fresh) |

### Interface Modes

| Flag | Interface | Description |
|------|-----------|-------------|
| (none) | Console | Progressive CLI output |
| `-i` | Interactive | REPL with commands |
| `-tui` | TUI | Textual terminal UI with themes |
| `-x` | GUI | Tkinter graphical interface |

### Examples

```bash
# Analyze a mega-cap household-products operator
lynx-staples -p PG

# Force fresh data download
lynx-staples -p KO --refresh

# Search by company name
lynx-staples -p "Procter & Gamble"

# Interactive mode
lynx-staples -p -i

# Export HTML report
lynx-staples -p MO --export html

# Explain a metric
lynx-staples --explain gross_margin

# Skip filings and news for faster analysis
lynx-staples -t COST --no-reports --no-news
```

## Analysis Sections

1. **Company Profile** — Tier, operator stage, staples sub-segment, market-exposure classification
2. **Sector & Industry Insights** — Staples-specific context and benchmarks
3. **Valuation Metrics** — Traditional (P/E, P/FCF, EV/EBITDA, P/S, dividend yield) + staples-specific (EV per store)
4. **Profitability Metrics** — ROE, ROIC, margins with trend, SG&A%, store-contribution proxy (hidden for pre-profit stages)
5. **Solvency & Survival** — Debt/EBITDA, lease-adjusted leverage, interest coverage, cash runway for emerging operators
6. **Growth & Capital Discipline** — Revenue / earnings growth, organic-growth proxy, capex intensity, dilution / buyback CAGR
7. **Operating Efficiency** — Asset turnover, inventory turnover, days inventory, revenue per employee, working-capital intensity
8. **Share Structure** — Outstanding/diluted shares, insider/institutional ownership
9. **Business Quality** — Brand strength, unit economics, financial position, defensive sensitivity, channel mix
10. **Intrinsic Value** — DCF, Dividend Discount Model, Graham Number, Asset-Based (method selection by stage)
11. **Market Intelligence** — Analysts, short interest, technicals, insider trades, XLP / sub-segment ETF context
12. **Financial Statements** — 5-year annual summary
13. **SEC Filings** — Downloadable regulatory filings
14. **News** — Yahoo Finance + Google News RSS
15. **Assessment Conclusion** — Weighted score, verdict, strengths/risks, screening checklist
16. **Consumer Staples Disclaimers** — Stage-specific risk disclosures

## Relevance System

Each metric is classified by importance for the operator's maturity stage:

| Level | Display | Meaning |
|-------|---------|---------|
| **Critical** | `*` bold cyan star | Must-check for this stage |
| **Relevant** | Normal | Important context |
| **Contextual** | Dimmed | Informational only |
| **Irrelevant** | Hidden | Not meaningful for this stage |

Example: For a Mature Defensive Operator, ROIC, dividend coverage, and Debt/EBITDA are **Critical** while Cash Runway is **Irrelevant**.

## Scoring Methodology

The overall score (0-100) is a weighted average of 5 categories, with weights adapted by both company tier AND operator stage:

| Stage                          | Valuation | Profitability | Solvency | Growth | Business Quality |
|--------------------------------|-----------|---------------|----------|--------|------------------|
| Early Stage                    | 5%        | 5%            | 40-45%   | 15-20% | 30%              |
| Emerging Staples Brand         | 5-10%     | 5-10%         | 30-40%   | 25%    | 25%              |
| Scaling Staples Operator       | 10-15%    | 10-20%        | 15-35%   | 25%    | 25%              |
| Mature Defensive Operator      | 15-20%    | 15-25%        | 10-30%   | 15-20% | 25%              |
| Brand Licensor / Asset-Light   | 20%       | 30%           | 10%      | 15%    | 25%              |

Verdicts: Strong Buy (>=75), Buy (>=60), Hold (>=45), Caution (>=30), Avoid (<30).

## Project Structure

```
lynx-investor-consumer-staples/
├── lynx-investor-consumer-staples.py       # Runner script
├── pyproject.toml                          # Build configuration
├── requirements.txt                        # Dependencies
├── img/                                    # Logo images
├── data/                                   # Production cache
├── data_test/                              # Testing cache
├── docs/                                   # Documentation
│   └── API.md                              # API reference
├── robot/                                  # Robot Framework tests
│   ├── cli_tests.robot
│   ├── api_tests.robot
│   └── export_tests.robot
├── tests/                                  # Unit tests
└── lynx_staples/                           # Main package
```

## Testing

```bash
# Unit tests
pytest tests/ -v

# Robot Framework acceptance tests
robot robot/
```

## License

BSD 3-Clause License. See LICENSE in source.

## Author

**Borja Tarraso** — borja.tarraso@member.fsf.org
