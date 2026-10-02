import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_example_home(home_page):
    home_page.load_fixture("<html><body><h1>Example Domain</h1></body></html>")
    assert home_page.heading() == "Example Domain"
