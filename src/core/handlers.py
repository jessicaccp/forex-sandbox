from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.exceptions import SameCurrencyError


async def same_currency_exception_handler(
    request: Request, exc: SameCurrencyError
):
    """Handles the SameCurrencyError by returning 400 Bad Request response."""
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message},
    )


def register_handlers(app: FastAPI):
    """Adds all custom exception handlers to the FastAPI application."""
    app.add_exception_handler(
        SameCurrencyError, same_currency_exception_handler
    )
