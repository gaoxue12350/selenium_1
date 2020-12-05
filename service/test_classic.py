#coding:utf-8
import datetime
import json
import requests

def test_tag_list():
    corpid='ww082c54990645602b'
    corpsecret='oVl-ssXZiKT_KqEi3AnoPyeBBzLYsWsV7NVBJLb6zew'
    r=requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                   params={'corpid':corpid,'corpsecret':corpsecret})
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    token=r.json()['access_token']

    r=requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={'access_token':token},
        json={'tag_id': []})
    print(json.dumps(r.json(),indent=2))
    assert r.status_code==200
    assert r.json()['errcode']==0

    tag_name="tag1_new"+str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    r=requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                    params={'access_token':token},
                    json={
                        "id": "etMoQQDQAACzSou6IVZVyDf33-zSC3ZQ",
                        "name": tag_name
                          }
                    )
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={'access_token': token},
        json={'tag_id': []})
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    tags=[tag
          for group in r.json()['tag_group'] if group['group_name'] == 'python15'
          for tag in group['tag'] if tag['name'] == tag_name
          ]
    assert tags !=[]

