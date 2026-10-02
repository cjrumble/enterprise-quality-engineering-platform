# Enterprise Quality Engineering Platform

A senior-level Python + Playwright + pytest reference framework showing how a Quality Engineering team can design **reusable automation, API/UI coverage, diagnostics, and CI quality gates**.

## Architecture
- Page Objects isolate UI behavior from test intent.
- HTTP client layer centralizes API transport and timeouts.
- Configuration supports environment-specific endpoints without changing test code.
- pytest markers separate UI/API/smoke/external coverage.
- Quality gates demonstrate release-blocking criteria.
- GitHub Actions executes the suite across supported Python versions and publishes JUnit evidence.

## Engineering practices
- deterministic, readable test intent
- reusable abstractions instead of duplicated request/browser code
- explicit timeouts and environment configuration
- parameterized status/boundary coverage
- CI test artifacts
- separation of test strategy, transport, page behavior, and assertions

## Run locally
```bash
pip install -r requirements.txt
playwright install chromium
pytest -v
```

## Portfolio scope
The external demo endpoints are intentionally non-production and safe for portfolio execution. The architecture can be pointed at an authenticated application under test through environment configuration.

## Hiring-manager evidence
This project demonstrates **automation architecture and engineering judgment**, not a collection of isolated scripts: reusable layers, CI quality gates, diagnostics, maintainability, and risk-oriented coverage.
