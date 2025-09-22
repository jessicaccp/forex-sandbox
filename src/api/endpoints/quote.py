from fastapi import APIRouter

from api.schemas.quote import QuoteResponse
from core import services

router = APIRouter()


@router.get("/quote", response_model=QuoteResponse)
async def get_quote(from_currency: str, to_currency: str):
    """Gets a simulated currency exchange quote."""

    return await services.create_simulated_quote(
        from_currency=from_currency, to_currency=to_currency
    )
