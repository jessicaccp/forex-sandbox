import importlib.metadata

from fastapi import FastAPI

from src.api.router import api_router
from src.core.handlers import register_handlers

__version__ = importlib.metadata.version("forex-sandbox")

app = FastAPI(
    title="Forex Sandbox API",
    description="A currency quote API built with FastAPI to showcase the \
        performance of asynchronous operations.",
    version=__version__,
    contact={
        "name": "Jessica Patricio",
        "url": "https://github.com/jessicaccp",
    },
)

register_handlers(app)
app.include_router(api_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
