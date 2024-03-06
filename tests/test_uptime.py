from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_endpoint():
    datasette = Datasette()
    response = await datasette.client.get("/-/uptime")
    assert response.status_code == 200
    assert list(response.json()) == ["started", "now", "uptime_seconds", "uptime_hours"]
