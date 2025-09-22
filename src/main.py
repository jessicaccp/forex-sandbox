from fastapi import FastAPI

from api.endpoints import quote

app = FastAPI(title="Forex Sandbox API")
app.include_router(quote.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
