import pytest, requests

@pytest.mark.api
def test_public_api_status():
    response=requests.get("https://httpbin.org/status/200",timeout=20)
    assert response.status_code==200
