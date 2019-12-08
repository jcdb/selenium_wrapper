from selenium.webdriver.support.ui import WebDriverWait
from os import environ
from component import log
from component.webdriver.remote import WebDriverRemote
from component.visitor import Visitor
from component.getter.html import GetterHtml
from component.getter.element import GetterElement

SLEEP_TIME = environ.get('SLEEP_TIME', 15)



class SeleniumWrapper:

    def __init__(self, web_driver=None):

        self._browser = web_driver or WebDriverRemote()
        self._wait = WebDriverWait(self._browser, SLEEP_TIME)
        log.info('Session started.')

    def visit(self, url, get_html: bool = False):
        Visitor.execute(self._browser, url)
        if get_html:
            return GetterHtml.execute(self._browser)

    def get_element(self, element_name, expected_condition, search_By):
        return GetterElement.execute(self._wait, element_name, expected_condition, search_By)
        # TODO CustomError - "SeleniumWrapperError" ?¿...


    def __exit__(self):
        # TODO Handling by Selenium-hub?¿
        log.progress(" To-DO Close browser")
        self._browser.quit()
        self._browser.close()