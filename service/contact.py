import json
import random
from datetime import datetime

import requests

from service.base_api import BaseApi


class Contact(BaseApi):
    corpid = 'ww082c54990645602b'
    corpsecret = '-4FqwCQdtQymn2g7EBhgsmgdDKC7lyFkYMLM2X15UyY'

    def __init__(self):
        self.token=self.get_token(self.corpid,self.corpsecret)

    #创建成员
    def create_member(self,userid,name,mobile,department):
        data={'method':'post',
              'url':'https://qyapi.weixin.qq.com/cgi-bin/user/create',
              'params':{'access_token':self.token},
              'json':{"userid": userid,
                       "name": name,
                       "mobile": mobile,
                       "department": department}
              }
        r=self.send(data)
        return r

    #随机生成手机号
    def generate_phone_number(self):
        header_list=["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189"]
        phone_number=random.choice(header_list)+''.join((random.choice('0123456789') for i in range(8)))
        return phone_number

    def create_member_detect(self,userid,name,mobile,department):
        userid=userid
        mobile=mobile
        r=self.create_member(userid,name,mobile,department)
        #mobile存在
        if r.json()['errcode']==60104:
            print(self.get_member(userid).json())
            mobile=self.get_member(userid).json()['mobile']
            if not mobile:
                return ''
            self.delete_member(userid)
            print('mobile存在,delete(userid):',f'{userid}')
            r=self.create_member(userid,name,mobile,department)
        #userid存在
        elif r.json()['errcode'] == 60102:
            user_id = self.get_member(userid).json()['userid']
            if not user_id:
                return ''
            self.delete_member(userid)
            print('userid已经存在,delete(userid):', f'{userid}')
            r=self.create_member(userid,name,mobile,department)
        return r

    #读取成员
    def get_member(self,userid):
        data={
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            'params':{'access_token':self.token,
                      'userid':userid}
                      }
        r=self.send(data)
        return r

    #{'errcode': 60111, 'errmsg': 'userid not found'}
    def get_member_detect(self,userid):
        r=self.get_member(userid)
        if r.json()['errcode']==60111:
            self.create_member_detect(userid,'name',self.generate_phone_number(),[1])
            r=self.get_member(userid)
        return r

    #更新成员
    def update_member(self,userid,name):
        data={
            'method':'post',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/user/update',
            'params':{'access_token':self.token},
            'json':{"userid": userid,
                    "name": name
            }
        }
        r=self.send(data)
        return r

    #删除成员
    def delete_member(self,userid):
        data={
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            'params':{'access_token':self.token,
                      'userid':userid},
        }
        r=self.send(data)
        return r

    #{'errcode': 60111, 'errmsg': 'userid not found}
    def delete_member_detect(self,userid):
        r=self.delete_member(userid)
        if r.json()['errcode']==60111:
            # print(self.get_member(userid).json()['errmsg'])
            if 'userid not found' in  self.get_member(userid).json()['errmsg']:
                self.create_member(userid,'name',self.generate_phone_number(),[1])
            r=self.delete_member(userid)
        return r

    #获取部门成员
    def department_memebers(self,department_id):
        data={
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist',
            'params':{'access_token':self.token,
                      'department_id':department_id
                      }
        }
        r=self.send(data)
        return r

    #获取部门成员详情
    def department_members_details(self,department_id):
        data={
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/user/list',
            'params':{'access_token':self.token,
                      'department_id':department_id
                      }
        }
        r=self.send(data)
        return r

