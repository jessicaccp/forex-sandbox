from fastapi import APIRouter

from src.api.endpoints import quote

api_router = APIRouter()
api_router.include_router(quote.router, prefix="/v1", tags=["Quote"])
