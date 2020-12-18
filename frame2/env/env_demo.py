import requests
import yaml


class Api:
    with open('env.yml') as f:
        env=yaml.safe_load(f)

    def send(self,data:dict):
        #替换url
        data['url']=str(data['url']).replace('testing-studio',self.env['testing-studio'][self.env['default']])
        # r=requests.request(method=data['method'],url=data['url'],headers=data['headers'])
        r=requests.request(**data)
        return r