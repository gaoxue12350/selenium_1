import datetime
import json
import requests

class Tag:
    def __init__(self):
        self.token=self.get_token()

    #获取token
    def get_token(self):
        corpid = 'ww082c54990645602b'
        corpsecret = 'oVl-ssXZiKT_KqEi3AnoPyeBBzLYsWsV7NVBJLb6zew'
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': corpid, 'corpsecret': corpsecret})
        # print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']
        return token

    #增加标签
    def add(self,tag_name,group_id=None,group_name=None,order=None):
        r=requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                        params={'access_token': self.token},
                        json={"group_id": group_id,"group_name": group_name,"order": 1,"tag":
                            [{"name": tag_name,"order": 1}]})
        # print(json.dumps(r.json(), indent=2))
        return r

    #获取标签
    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={'tag_id': []})
        print(json.dumps(r.json(), indent=2))
        return r

    #更新标签
    def update(self,id,tag_name):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                          params={'access_token': self.token},
                          json={"id": id,"name": tag_name})
        # print(json.dumps(r.json(), indent=2))
        return r

    #删除标签
    def delete(self,tag_id=None,group_id=None):
        r=requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                        params={'access_token': self.token},
                        json={"tag_id": tag_id,
                            "group_id": group_id})
        return r

    #已知tagName，获取groupName
    def tagName_groupName(self,tag_name):
        r=self.list()

