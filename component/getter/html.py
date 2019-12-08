from component import log


class GetterHtml:

    @staticmethod
    def execute(browser):
        try:
            return browser.page_source
        except Exception as error:
            log.error(error)
