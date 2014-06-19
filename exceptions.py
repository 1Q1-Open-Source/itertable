try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None


class IoException(Exception):
    def __str__(self):
        return self.message or self.__doc__


class LoadFailed(IoException):
    """Error loading data!"""

    def __init__(self, message, path=None, code=None):
        super(LoadFailed, self).__init__(message)
        self.path = path
        self.code = code

    def __str__(self):
        if self.message:
            text = self.message
            if '<' in text and '>' in text and BeautifulSoup:
                html = BeautifulSoup(text).body
                if html:
                    text = html.get_text('\n')
            return text
        elif self.code is not None:
            return "%s Error" % self.code
        return super(LoadFailed, self).__str__()


class ParseFailed(IoException):
    """Error parsing data!"""
    pass


class MappingFailed(IoException):
    """Error processing data!"""
    pass


class NoData(IoException):
    """No data returned!"""
    pass
