from datetime import datetime

from fastapi import APIRouter

from api.schemas.quote import QuoteResponse

router = APIRouter()


@router.get("/quote", response_model=QuoteResponse)
async def get_quote(from_currency: str, to_currency: str):
    """Returns a simulated currency exchange quote."""

    return {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "rate": 5.23,
        "timestamp": datetime.now(),
    }
