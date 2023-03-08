import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.hold_browser_open = True
    browser.config.window_width = '1980'
    browser.config.window_height = '1024'
    browser.config.timeout = 6.0

    yield
