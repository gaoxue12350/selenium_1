from frame2.env.env_demo import Api

class TestApi:
    data = {
        'method': 'get',
        'url': 'http://testing-studio:9999/demo64.txt',
        'headers': None,
    }

    def test_send(self):
        api=Api()
        r=api.send(self.data)
        print(r.text)