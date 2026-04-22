"""Tests for the consumer-staples sector validation gate."""

import pytest
from lynx_staples.core.analyzer import _validate_sector, SectorMismatchError
from lynx_staples.models import CompanyProfile


class TestSectorValidation:
    """Sector validation blocks non-consumer-staples companies."""

    def _profile(self, ticker="T", sector=None, industry=None, desc=None):
        return CompanyProfile(
            ticker=ticker, name=f"{ticker} Corp",
            sector=sector, industry=industry, description=desc,
        )

    # --- Should ALLOW ---
    def test_consumer_defensive_sector(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Packaged Foods"))

    def test_consumer_staples_sector(self):
        _validate_sector(self._profile(sector="Consumer Staples", industry="Household & Personal Products"))

    def test_packaged_foods_industry(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Packaged Foods"))

    def test_beverages_non_alcoholic_industry(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Beverages - Non-Alcoholic"))

    def test_beverages_brewers_industry(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Beverages - Brewers"))

    def test_tobacco_industry(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Tobacco"))

    def test_household_personal_products_industry(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Household & Personal Products"))

    def test_grocery_stores_industry(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Grocery Stores"))

    def test_discount_stores_industry(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Discount Stores"))

    def test_pharmaceutical_retailers_industry(self):
        _validate_sector(self._profile(sector="Consumer Defensive", industry="Pharmaceutical Retailers"))

    def test_dividend_aristocrat_in_description(self):
        _validate_sector(self._profile(
            sector="Other", industry="Other",
            desc="Dividend Aristocrat operating across packaged food categories"))

    def test_grocery_in_description(self):
        _validate_sector(self._profile(
            sector="Other", industry="Other",
            desc="Operates a national chain of supermarket and grocery stores"))

    def test_tobacco_in_description(self):
        _validate_sector(self._profile(
            sector="Other", industry="Other",
            desc="Global manufacturer of cigarette and reduced-risk nicotine products"))

    def test_household_in_description(self):
        _validate_sector(self._profile(
            sector="Other", industry="Other",
            desc="Maker of household products including laundry detergent and cleaning products"))

    # --- Should BLOCK ---
    def test_technology_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Technology", industry="Software"))

    def test_financial_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Financial Services", industry="Banks"))

    def test_healthcare_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Healthcare", industry="Drug Manufacturers"))

    def test_basic_materials_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Basic Materials", industry="Gold"))

    def test_energy_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Energy", industry="Oil & Gas E&P"))

    def test_real_estate_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Real Estate", industry="REIT"))

    def test_consumer_cyclical_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Consumer Cyclical", industry="Specialty Retail"))

    def test_consumer_discretionary_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Consumer Discretionary", industry="Apparel Manufacturing"))

    def test_all_none_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile())

    def test_empty_strings_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="", industry="", desc=""))

    def test_error_message_content(self):
        with pytest.raises(SectorMismatchError, match="outside the scope"):
            _validate_sector(self._profile(sector="Technology", industry="Software"))

    def test_error_suggests_another_agent(self):
        """Wrong-sector warning appends a 'use lynx-investor-*' line."""
        with pytest.raises(SectorMismatchError) as exc:
            _validate_sector(self._profile(
                sector="Healthcare", industry="Biotechnology"))
        message = str(exc.value)
        assert "Suggestion" in message
        assert "lynx-investor-healthcare" in message

    def test_error_never_suggests_self(self):
        """The suggestion never points back to this agent itself."""
        with pytest.raises(SectorMismatchError) as exc:
            _validate_sector(self._profile(
                sector="Energy", industry="Uranium"))
        message = str(exc.value)
        assert "use 'lynx-investor-consumer-staples'" not in message
