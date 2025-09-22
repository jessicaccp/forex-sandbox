import pytest

from src.api.schemas.quote import QuoteResponse
from src.core import services
from src.core.exceptions import SameCurrencyError


@pytest.mark.asyncio
async def test_create_simulated_quote_success():
    """Tests if the service successfully creates a quote for different currencies."""  # noqa: E501

    quote = await services.create_simulated_quote(
        from_currency="USD", to_currency="BRL"
    )
    assert isinstance(quote, QuoteResponse)
    assert quote.from_currency == "USD"
    assert quote.to_currency == "BRL"
    assert isinstance(quote.rate, float)


@pytest.mark.asyncio
async def test_create_simulated_quote_same_currency_error():
    """Tests if the service correctly raises an error for same currencies."""

    with pytest.raises(SameCurrencyError):
        await services.create_simulated_quote(
            from_currency="USD", to_currency="USD"
        )
