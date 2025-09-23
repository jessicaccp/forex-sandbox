import pytest
from httpx import ASGITransport, AsyncClient, codes

from src.main import app

TEST_AMOUNT = 150.0


@pytest.mark.asyncio
async def test_get_quote_success():
    """Tests the /v1/quote endpoint for a successful response."""

    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport, base_url="http://test"
    ) as client:
        response = await client.get(
            "/v1/quote?from_currency=USD&to_currency=BRL&amount=150"
        )

    assert response.status_code == codes.OK
    data = response.json()
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "BRL"
    assert data["amount"] == TEST_AMOUNT


@pytest.mark.asyncio
async def test_get_quote_same_currency_error():
    """Tests the /v1/quote endpoint for the expected 400 error."""

    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport, base_url="http://test"
    ) as client:
        response = await client.get(
            "/v1/quote?from_currency=USD&to_currency=USD&amount=150"
        )

    assert response.status_code == codes.BAD_REQUEST
    data = response.json()
    assert "detail" in data
    assert (
        "'from_currency' and 'to_currency' cannot be the same"
        in data["detail"]
    )
