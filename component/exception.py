class SeleniumWrapperError(Exception):
    """Base class for other exceptions"""
    pass


class InvalidUrlError(SeleniumWrapperError):
    """Raised when the input url is not valid"""
    pass
