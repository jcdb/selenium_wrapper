from selenium.common.exceptions import InvalidArgumentException, WebDriverException
from component import log
from component.exception import InvalidUrlError

class Visitor:

    @staticmethod
    def execute(browser, url):
        try:
            log.info(f"Request to URL: {url}")
            browser.get(url)
        except (InvalidArgumentException, WebDriverException) as error:
            log.exception(f"Malformed URL or Reached error page: {url} is not a valid URL.")
            raise InvalidUrlError(error)
