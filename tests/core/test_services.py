import pytest

from src.core import services
from src.core.exceptions import SameCurrencyError

TEST_AMOUNT = 100.0


@pytest.mark.asyncio
async def test_create_simulated_quote_success():
    """Tests if the service creates a quote for different currencies."""

    quote = await services.create_simulated_quote(
        from_currency="USD", to_currency="BRL", amount=100.0
    )

    assert quote.from_currency == "USD"
    assert quote.to_currency == "BRL"
    assert quote.amount == TEST_AMOUNT
    assert quote.converted_amount > 0
    assert quote.exchange_rate > 0


@pytest.mark.asyncio
async def test_create_simulated_quote_same_currency_error():
    """Tests if the service correctly raises an error for same currencies."""

    with pytest.raises(SameCurrencyError):
        await services.create_simulated_quote(
            from_currency="USD", to_currency="USD", amount=100.0
        )
