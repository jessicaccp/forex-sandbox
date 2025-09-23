from typing import Annotated

from fastapi import APIRouter, Query

from src.api.schemas.quote import QuoteResponse
from src.core import services

router = APIRouter()


@router.get(
    "/quote",
    response_model=QuoteResponse,
    summary="Gets a simulated currency exchange quote",
    description="Returns a simulated quote for converting an amount between \
        two currencies.",
)
async def get_quote(
    from_currency: Annotated[
        str,
        Query(
            description="Source currency code (e.g., USD, BRL)",
            examples=["USD"],
            min_length=3,
            max_length=3,
        ),
    ],
    to_currency: Annotated[
        str,
        Query(
            description="Destination currency code (e.g., EUR, JPY)",
            examples=["BRL"],
            min_length=3,
            max_length=3,
        ),
    ],
    amount: Annotated[
        float,
        Query(
            description="The amount to be converted.",
            examples=[100.50],
            gt=0,
        ),
    ],
):
    return await services.create_simulated_quote(
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
    )
