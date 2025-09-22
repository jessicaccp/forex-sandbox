import asyncio
import random
from datetime import datetime

from src.api.schemas.quote import QuoteResponse
from src.core.exceptions import SameCurrencyError


async def create_simulated_quote(
    from_currency: str, to_currency: str
) -> QuoteResponse:
    """Business logic to simulate a currency exchange quote."""

    if from_currency.strip().upper() == to_currency.strip().upper():
        raise SameCurrencyError()

    delay = random.uniform(0.5, 1.5)
    await asyncio.sleep(delay)
    rate = random.uniform(4.8, 5.3)

    return QuoteResponse(
        from_currency=from_currency,
        to_currency=to_currency,
        rate=round(rate, 4),
        timestamp=datetime.now(),
    )
