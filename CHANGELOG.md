# Changelog

## [4.0] - 2026-04-23

Part of **Lince Investor Suite v4.0** coordinated release.

### Added
- URL-safety enforcement for every RSS-sourced news URL and every
  `webbrowser.open(...)` site — powered by
  `lynx_investor_core.urlsafe`.
- Sector-specific ASCII art in easter-egg visuals (replaces the shared
  pickaxe motif that leaked into non-mining sectors).

### Changed
- Aligned every user-visible sector string with the package's real
  sector: titles, subtitles, app class names, splash taglines, news
  keywords, User-Agent headers, themes, export headers, and fortune
  quotes no longer carry template leftovers.
- Depends on `lynx-investor-core>=4.0`.

All notable changes to **Lynx Consumer Staples Analysis** are documented here.

## [3.0] - 2026-04-22

Part of **Lince Investor Suite v3.0** coordinated release.

### Added
- Uniform PageUp / PageDown navigation across every UI mode (GUI, TUI,
  interactive, console). Scrolling never goes above the current output
  in interactive and console mode; Shift+PageUp / Shift+PageDown remain
  reserved for the terminal emulator's own scrollback.
- Sector-mismatch warning now appends a `Suggestion: use
  'lynx-investor-<other>' instead.` line sourced from
  `lynx_investor_core.sector_registry`. The original warning text is
  preserved as-is.

### Changed
- TUI wires `lynx_investor_core.pager.PagingAppMixin` and
  `tui_paging_bindings()` into the main application.
- Graphical mode binds `<Prior>` / `<Next>` / `<Control-Home>` /
  `<Control-End>` via `bind_tk_paging()`.
- Interactive mode pages long output through `console_pager()` /
  `paged_print()`.
- Depends on `lynx-investor-core>=2.0`.

## [1.0] — 2026-04-22

Initial release as a standalone agent in the Lince Investor Suite. Forked
from `lynx-investor-consumer-discretionary` (shared plumbing in
`lynx-investor-core`) and specialized for consumer staples companies.

### Added — Consumer-Staples Fundamental Analysis

- **Sector validator** restricts analysis to consumer-staples (GICS:
  "Consumer Defensive" in Yahoo Finance taxonomy) companies, with
  allow-lists for packaged foods, non-alcoholic and alcoholic beverages,
  tobacco, household and personal-care products, food retail, hypermarkets
  / discount stores, drug retail, and agribusiness.
- **Stage classifier** labels operators Early Stage / Pre-Profit, Emerging
  Staples Brand, Scaling Staples Operator, Mature Defensive Operator, or
  Brand Licensor / Asset-Light based on revenue scale, operating margin,
  and description heuristics.
- **Sub-segment classifier** maps companies to Packaged Food, Non-Alcoholic
  Beverages, Alcoholic Beverages, Tobacco, Household Products, Personal
  Products, Food Retail, Hypermarkets & Super Centers, Drug Retail, or
  Agribusiness.
- **Market-exposure tier** measures geographic revenue-concentration risk
  (developed / mixed / high concentration).
- **Staples-specific metrics**:
  - Gross margin trend (expanding / stable / compressing)
  - Organic-growth proxy (revenue growth minus asset growth)
  - Lease-adjusted leverage (Debt + 8× rent) / EBITDAR
  - SG&A as % of revenue (advertising-intensity indicator)
  - Store-contribution margin proxy (food retail / hypermarket)
  - Inventory turnover + days inventory
  - Working-capital intensity (negative WC = Costco-style favorable)
  - Revenue per employee
  - CAPEX intensity
- **Business-quality scoring** over five dimensions:
  - Brand strength / margin resilience (25 pts) — staples-calibrated
    thresholds (>50% premium / 38-50% strong / 25-38% moderate)
  - Unit economics — ROIC + operating margin (25 pts)
  - Financial position — leverage + liquidity (20 pts)
  - Management alignment — insider ownership (15 pts)
  - Capital discipline — dilution / buybacks (15 pts)
- **Defensive-sensitivity tagging** distinguishes inelastic staples
  (tobacco, packaged food, household products) from modestly cyclical
  sub-segments (food/drug retail, agribusiness).
- **10-point consumer staples screening checklist**: positive operating
  margin, gross margin ≥ 30%, ROIC > 10%, reasonable leverage, revenue
  growth > 3%, low dilution (< 3%/yr), insider ownership ≥ 5%, positive
  FCF margin, reasonable P/E (< 25), developed-market exposure.
- **Stage-appropriate intrinsic-value methods**: DCF + Dividend Discount
  Model for mature defensive operators; EV/EBITDA comps for scaling;
  EV/Revenue with margin ramp for emerging; DCF on royalty stream for
  brand licensors.
- **Sector context** now fetches the Consumer Staples Select Sector SPDR
  (XLP) as the defensive demand proxy, plus a sub-segment peer ETF (PBJ
  for food & beverage, IYK for US staples, FTXG for food, MOO for
  agribusiness).
- **Consumer-staples disclaimers** cover private-label substitution,
  GLP-1 demand drag, input-cost inflation, regulatory pressure (sugar
  tax, plain packaging), and channel disruption.

### Changed

- `CompanyStage` enum string values updated: `GRASSROOTS="Early Stage / Pre-Profit"`,
  `EXPLORER="Emerging Staples Brand"`, `DEVELOPER="Scaling Staples Operator"`,
  `PRODUCER="Mature Defensive Operator"`, `ROYALTY="Brand Licensor / Asset-Light"`.
- `Segment` enum redefined with consumer staples sub-segments (Packaged
  Food, Beverages NA / Alc, Tobacco, Household, Personal, Food Retail,
  Hypermarket, Drug Retail, Agribusiness).
- `BusinessQualityIndicators` re-tuned for staples — defensive sensitivity
  tag, brand-strength thresholds calibrated for staples gross margins.
- Scoring weights rebalanced: mature / brand-licensor operators weight
  profitability and business quality at 25% each; emerging / early-stage
  operators keep solvency + growth dominance.
- All sector insights, metric explanations, and peer examples rewritten
  for consumer-staples context (PG, KO, PEP, MO, COST, etc.).

### Infrastructure

- Shared plumbing continues to come from `lynx-investor-core` (storage,
  sector gate, ticker resolution, logo, about, easter-egg renderer).
