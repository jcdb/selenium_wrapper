import pytest
from component.webdriver.remote import WebDriverRemote
from component.visitor import Visitor
from component.exception import InvalidUrlError


@pytest.fixture
def browser():
    return WebDriverRemote()


def test_visitor_url_valid(browser):
    url_valid = "https://www.python.org/"
    visit = Visitor.execute(browser, url_valid)
    assert visit is None


def test_visitor_url_invalid(browser):
    url_invalid = "ht://www.python.org/"
    with pytest.raises(InvalidUrlError):
        Visitor.execute(browser, url_invalid)
