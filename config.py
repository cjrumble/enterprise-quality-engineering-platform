from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("QE_BASE_URL", "https://example.com")
    api_url: str = os.getenv("QE_API_URL", "https://httpbin.org")
    timeout_seconds: float = float(os.getenv("QE_TIMEOUT_SECONDS", "20"))

settings = Settings()
