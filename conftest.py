import pytest
from playwright.sync_api import Page

@pytest.fixture
def home_page(page: Page):
    from pages.home_page import HomePage
    return HomePage(page)
