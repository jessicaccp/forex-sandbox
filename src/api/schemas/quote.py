from datetime import datetime

from pydantic import BaseModel


class QuoteResponse(BaseModel):
    from_currency: str
    to_currency: str
    rate: float
    timestamp: datetime
