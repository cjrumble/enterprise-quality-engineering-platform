# Enterprise Quality Engineering Platform

A portfolio-grade Python + Playwright + pytest framework demonstrating UI/API automation, risk-based coverage, reusable fixtures, evidence capture, and CI quality gates.

## Architecture
- `tests/ui`: browser workflows
- `tests/api`: REST contract/smoke tests
- `pages`: page-object abstractions
- `api`: API client layer
- `fixtures`: reusable test data and browser fixtures
- `.github/workflows`: CI execution

## Quality strategy
The framework favors stable user-facing locators, explicit API assertions, negative/boundary coverage, deterministic test data, trace/screenshot capture on failure, and fast feedback in CI.

## Run
```bash
pip install -r requirements.txt
playwright install chromium
pytest -m smoke -v
pytest -v
```

The included demo tests use a public sample site/API and are intentionally safe to run.

## Hiring-manager evidence
This project demonstrates test architecture, automation engineering, API/UI integration, failure diagnostics, CI/CD, and quality-gate thinking rather than a collection of isolated scripts.
