from frame2.test_requests import ApiRequest


class TestApiRequest:
    # req_data = {
    #     "method": "get",
    #     "url": "http://127.0.0.1:9999/demo64.txt",
    #     "headers": None,
    #     "encoding": "base64"
    # }
    def test_send(self,req_data):
        a=ApiRequest()
        print(a.send(req_data))
