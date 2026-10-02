import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_example_home(home_page):
    home_page.open()
    assert home_page.heading() == "Example Domain"
