"""HTTP response class"""


class HttpResponse:
    """A Class to hold request content and response time"""
    def __init__(self):
        """Initialize content and response time"""
        self._content = ''
        self._response_time = ''

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def response_time(self):
        return self._response_time

    @response_time.setter
    def response_time(self, value):
        self._response_time = value

    def print_response_time(self):
        """Print response time in certain format"""
        return f'HttpResponse{{response time = {self.response_time}ms }}'

    def print_response_content(self):
        """Print response content in certain format"""
        return f'HttpResponse{{response content = {self.content} }}'


if __name__ == '__main__':
    hr = HttpResponse()
    hr.print_response_time()
