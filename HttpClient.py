import requests
import HttpResponse


class HttpClient:
    def __init__(self, url):
        self.url = url

    def send_request(self) -> HttpResponse:
        """Send request to url

        :return: HttpResponse obj
        """
        response = HttpResponse.HttpResponse()
        try:
            request = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        response.content = request.content
        response.response_time = request.elapsed.total_seconds()
        return response
