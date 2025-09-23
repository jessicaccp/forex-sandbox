from datetime import datetime

from pydantic import BaseModel, Field


class QuoteResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float = Field(
        ..., description="The original amount to be converted."
    )
    exchange_rate: float = Field(
        ..., description="The simulated exchange rate."
    )
    converted_amount: float = Field(
        ..., description="The resulting amount after conversion."
    )
    timestamp: datetime
