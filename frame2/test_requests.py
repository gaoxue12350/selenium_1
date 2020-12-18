import json
import requests
import base64

class ApiRequest:

    def send(self,data:dict):
        r=requests.request(data['method'],data['url'],headers=data['headers'])
        if data['encoding']=='base64':
            return json.loads(base64.b64decode(r.content))
        elif data['encoding']=='private':
            return requests.post("url",data=r.content)
