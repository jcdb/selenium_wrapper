from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from component import log


class GetterElement:

    @staticmethod
    def execute(_wait, element_name, expected_condition, search_By):
        try:
            expected_condition = getattr(ec, expected_condition)
            search_by = getattr(By, search_By)
            element = _wait.until(expected_condition((search_by, element_name)))
            return element
        except (NoSuchWindowException, WebDriverException) as error:
            log.exception(f'Unexpected crash on web.driver, check it out: {error}.')
        except AttributeError as error:
            log.exception(f'Some of the search parameters are wrong: {error}.')
            # TODO CustomError - "SeleniumWrapperError" ?¿...
