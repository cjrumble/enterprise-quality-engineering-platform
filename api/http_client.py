from dataclasses import dataclass
import requests

@dataclass
class ApiResponse:
    status_code: int
    json_body: object | None
    headers: dict

class HttpClient:
    def __init__(self, base_url: str, timeout: float = 20):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str) -> ApiResponse:
        response = requests.get(f"{self.base_url}/{path.lstrip('/')}", timeout=self.timeout)
        try:
            body = response.json()
        except ValueError:
            body = None
        return ApiResponse(response.status_code, body, dict(response.headers))
