import HttpClient
import HttpResponse


class LoadTester:
    def __init__(self, url, sbc, times):
        self.url = url
        self.times = times

    def test_url(self):
        resp_list = []
        for i in range(self.times):
            client = HttpClient.HttpClient(self.url)
            resp = client.send_request()
            resp_list.append(resp)
        return resp_list

    @staticmethod
    def get_average_response_time(response_list):
        total_time, size = 0, len(response_list)
        for resp in response_list:
            total_time += resp.response_time
        return total_time/size
