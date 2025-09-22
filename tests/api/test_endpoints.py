import pytest
from httpx import ASGITransport, AsyncClient, codes

from src.main import app


@pytest.mark.asyncio
async def test_get_quote_success():
    """Tests the /v1/quote endpoint for a successful response."""

    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport, base_url="http://test"
    ) as client:
        response = await client.get(
            "/v1/quote?from_currency=USD&to_currency=BRL"
        )

    assert response.status_code == codes.OK
    data = response.json()
    assert data["from_currency"] == "USD"
    assert "rate" in data


@pytest.mark.asyncio
async def test_get_quote_same_currency_error():
    """Tests the /v1/quote endpoint for the expected 400 error."""

    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport, base_url="http://test"
    ) as client:
        response = await client.get(
            "/v1/quote?from_currency=USD&to_currency=USD"
        )

    assert response.status_code == codes.BAD_REQUEST
    assert "cannot be the same" in response.json()["detail"]
