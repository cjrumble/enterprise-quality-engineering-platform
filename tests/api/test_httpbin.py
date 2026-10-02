import pytest
from config import settings
from api.http_client import HttpClient

@pytest.mark.api
@pytest.mark.external
def test_public_api_status():
    client = HttpClient(settings.api_url, settings.timeout_seconds)
    response = client.get("/status/200")
    assert response.status_code == 200

@pytest.mark.api
@pytest.mark.external
@pytest.mark.parametrize("status", [200, 201, 204])
def test_expected_http_statuses(status):
    client = HttpClient(settings.api_url, settings.timeout_seconds)
    response = client.get(f"/status/{status}")
    assert response.status_code == status
