from os import environ
from selenium import webdriver

HOST_HUB = environ.get('HOST_HUB', '127.0.0.1')
PORT_HUB = environ.get('PORT_HUB', 4444)


class WebDriverRemote(webdriver.Remote):

    def __init__(self):
        selenium_grid_url = f"{HOST_HUB}:{PORT_HUB}/wd/hub"
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        self._driver = webdriver.Remote.__init__(self, desired_capabilities=capabilities, command_executor=selenium_grid_url)

    def __exit__(self):
        self._driver.quit()