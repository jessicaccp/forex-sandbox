import asyncio
import random
from datetime import datetime

from fastapi import APIRouter

from api.schemas.quote import QuoteResponse
from core.exceptions import SameCurrencyError

router = APIRouter()


@router.get("/quote", response_model=QuoteResponse)
async def get_quote(from_currency: str, to_currency: str):
    """Returns a simulated currency exchange quote after a async delay."""

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
