from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from component import log


class Visitor:

    @staticmethod
    def execute(browser, url):
        try:
            log.info(f"Request to URL: {url}")
            browser.get(url)
        except (InvalidArgumentException, WebDriverException):
            log.exception(f"Malformed URL or Reached error page: {url} is not a valid URL.")
            # TODO ERRORS
