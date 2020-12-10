import datetime
import json
import requests
from jsonpath import jsonpath
from service.base_api import BaseApi

class Tag(BaseApi):

    def __init__(self):
        super().__init__()

    # 获取标签
    def list(self):
        data={
            'method':'post',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'params':{'access_token': self.token_tag},
            'json':{'tag_id': []}
        }
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        #     params={'access_token': self.token},
        #     json={'tag_id': []})
        r=self.send(data)
        print(json.dumps(r.json(),ensure_ascii=False, indent=2))
        return r

    #更新标签
    def update(self,id,tag_name):
        data={
            'method':'post',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'params':{'access_token': self.token_tag},
            'json':{"id": id,"name": tag_name}
        }
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        #                   params={'access_token': self.token},
        #                   json={"id": id,"name": tag_name})
        # print(json.dumps(r.json(), indent=2))
        r=self.send(data)
        return r

    #判断group_name是否存在
    def find_group_id_by_name(self,group_name):
        r=self.list()
        #查询组名是否存在，如果不存在，报错
        for group in self.list().json()['tag_group']:
            if group_name in group['group_name']:
                return group['group_id']
        print('group_name not in group')
        #todo:如果group_id是空，也会类似false
        # return ValueError('group_name not in group')
        return ''

    def find_tag_id_by_name(self,tag_name):
        tag_id=jsonpath(self.list().json(),f'$..[?(@.name=="{tag_name}")]')[0]['id']
        return tag_id

    def is_group_id_exist(self,group_id):
        for group in self.list().json()['tag_group']:
            if group_id in group['group_id']:
                return True
            print("group_id not in group")
        return False

    # 增加标签
    # 异常："errcode": 40071,"errmsg": "UserTag Name Already Exist
    # 解决办法：1.删除对应tag  2.已有tagname基础上修改名称（时间戳、计数器）
    def add(self,group_name,tag,**kwargs):
        data={
            'method':'post',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'params':{'access_token': self.token_tag},
            'json':{"group_name": group_name,
                    "tag": tag,
                    **kwargs
                    }
        }
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        #                   params={'access_token': self.token},
        #                   json={"group_name": group_name,
        #                         "tag": tag,
        #                         **kwargs
        #                         })
        r=self.send(data)
        # print(json.dumps(r.json(), ensure_ascii=False,indent=2))
        return r

    def add_and_detect(self,group_name,tag,**kwargs):
        r=self.add(group_name,tag,**kwargs)
        #如果要添加的名称已经存在
        if r.json()['errcode']==40071:
            group_id=self.find_group_id_by_name(group_name)
            if not group_id:
                return ''
            self.delete_group([group_id])
            self.add(group_name,tag,**kwargs)
        result=self.find_group_id_by_name(group_name)
        if not result:
            print('add not success')
        return result

    def generate_unique_tag_name(self,tag_name):
        tag_name1=tag_name + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        return tag_name1

    #查询tag_id ->删除tag_id
    #如果正常：成功 {"errcode": 0,"errmsg": "ok"}
    #如果异常：失败 {"errcode": 40068,"errmsg": "invalid tagid}
    #1.删除接口有问题
    #2.进行重试（n）
    # 2.1添加一个接口，
    # 2.2添加的接口进行删除
    # 2.3再查询删除是否成功
    def delete_group(self,group_id):
        data={
            'method':'post',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params':{'access_token': self.token_tag},
            'json':{"group_id": group_id}
        }
        # r=requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #                 params={'access_token': self.token},
        #                 json={"group_id": group_id})
        r=self.send(data)
        print(json.dumps(r.json(),ensure_ascii=False,indent=2))
        return r

    def delete_tag(self,tag_id):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params': {'access_token': self.token_tag},
            'json': {"tag_id": tag_id}
        }
        # r=requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #                 params={'access_token': self.token},
        #                 json={"tag_id": tag_id})
        r=self.send(data)
        print(json.dumps(r.json(),ensure_ascii=False, indent=2))
        return r

    def delete_and_detect_group(self,group_ids):
        delete_group_ids=[]
        r=self.delete_group(group_ids)
        if r.json()['errcode']==40068:
            #如果标签不存在，就添加一个标签，将存入标签组
            for group_id in group_ids:
                if not self.is_group_id_exist(group_id):
                    group_id=self.add_and_detect('tmp123',[{'name':'1231'}])
                    delete_group_ids.append(group_id)
                #如果标签存在，就存入标签组
                else:
                    delete_group_ids.append(group_id)
            r=self.delete_group(delete_group_ids)
        return r

    def is_tag_id_exist(self,tag_id):
        # print(json.dumps(self.list().json()['tag_group'],indent=2))
        for group in self.list().json()['tag_group']:
            for tag in group['tag']:
                if tag_id in tag['id']:
                    return tag_id
            print('tag_id not in tag')
        return False

    def delete_and_detect_tag(self,tag_ids):
        delete_tag_id=[]
        r=self.delete_tag(tag_ids)
        if r.json()['errcode']==40068:
            r=self.list()
            # print(json.dumps(r.json(),ensure_ascii=False, indent=2))
            for tag_id in tag_ids:
                if not self.is_tag_id_exist(tag_id):
                    tag_name=self.generate_unique_tag_name('tag')
                    self.add_and_detect('tmp123',[{'name':tag_name}])
                    tag_id=self.find_tag_id_by_name(tag_name)
                    delete_tag_id.append(tag_id)
                else:
                    delete_tag_id.append(tag_id)
            r=self.delete_tag(delete_tag_id)
        return r

    #已知tagName，获取groupid
    def tagName_groupid(self,tag_name1,r):
        # r=self.list()
        tags = []
        tags_all = []
        tagname = []
        group_id1 = []
        tag_name1 = jsonpath(r.json(), f'$..[?(@.name=="{tag_name1}")]')
        group_id = jsonpath(r.json(), f'$..[?(@.group_id)]')
        # 取出所有标签存到tags_all中
        for i in group_id:
            # print(i['tag'])
            tags.append(i['tag'])
        # print(tags)
        for i in tags:
            for j in i:
                tags_all.append(j)
        # 如果已知的标签在tags_all中，将name存到tagname中
        for i in tag_name1:
            if i in tags_all:
                tagname.append(i['name'])
        for i in group_id:
            for x in i['tag']:
                # print("{i['tag'][0]['name']}:", f"'{i['tag'][0]['name']}'")
                for j in tagname:
                    if j in x['name']:
                        group_id1.append(i['group_id'])
        return group_id1[0]