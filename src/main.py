from fastapi import FastAPI

from api.router import api_router
from core.handlers import register_handlers

app = FastAPI(title="Forex Sandbox API")
register_handlers(app)
app.include_router(api_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
