import asyncio
import hashlib
import random
from datetime import datetime

from src.api.schemas.quote import QuoteResponse
from src.core.exceptions import SameCurrencyError


def _generate_deterministic_rate(
    from_currency: str, to_currency: str
) -> float:
    """Generates a consistent exchange rate based on currency pairs."""

    pair_string = f"{from_currency.upper()}{to_currency.upper()}"
    hash_object = hashlib.sha256(pair_string.encode())
    seed = int.from_bytes(hash_object.digest()[:4], "big")
    pseudo_random = random.Random(seed)
    rate = pseudo_random.uniform(0.5, 10.0)
    return round(rate, 4)


async def create_simulated_quote(
    from_currency: str, to_currency: str, amount: float
) -> QuoteResponse:
    """Business logic to simulate a currency exchange quote."""

    if from_currency.strip().upper() == to_currency.strip().upper():
        raise SameCurrencyError()

    delay = random.uniform(0.1, 0.5)
    await asyncio.sleep(delay)

    exchange_rate = _generate_deterministic_rate(from_currency, to_currency)
    converted_amount = round(amount * exchange_rate, 2)

    return QuoteResponse(
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
        exchange_rate=exchange_rate,
        converted_amount=converted_amount,
        timestamp=datetime.now(),
    )
