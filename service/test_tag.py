#coding:utf-8
import datetime
import uuid

import pytest
from jsonpath import jsonpath
from service.tag import Tag

class TestTag:
    def setup(self):
        self.tag = Tag()

    #删除标签组
    def test_delete_and_detect_group(self):
        r=self.tag.delete_and_detect_group(['etMoQQDQAACquqZ5jT9KwvfE10T46GYQ'])
        print(r.json(),type(r.json()))
        assert r.json()['errcode']==0

    #更新标签
    # @pytest.mark.skip(reason='skip')
    @pytest.mark.parametrize("tag_id,tag_name",[
        ('etMoQQDQAAu47atKWLSSXFVYmy8doqiA', 'tag1_new_'),
        ('etMoQQDQAAu47atKWLSSXFVYmy8doqiA', 'tag1_中文'),
        ('etMoQQDQAAu47atKWLSSXFVYmy8doqiA', 'tag1_[中文]')
    ])
    def test_update(self,tag_id,tag_name):
        # group_name='python15'
        # tag_id='etMoQQDQAACzSou6IVZVyDf33-zSC3ZQ'
        tag_name=tag_name+str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

        # r=self.tag.list()
        r=self.tag.update(id=tag_id,
                     tag_name=tag_name)
        r=self.tag.list()
        print(r.json(),type(r.json()))
        # print(type(jsonpath(r.json(),f"$..[?(@.name=='{tag_name}')]")))
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
        # tags=[tag
        #       for group in r.json()['tag_group'] if group['group_name'] == group_name
        #       for tag in group['tag'] if tag['name'] == tag_name
        #       ]
        # assert tags !=[]

    #增加标签
    # @pytest.mark.parametrize("tag_name,group_id",[
    #     ('tag_name中文', 'etMoQQDQAA_Lca86F1dGKme-4qde0VJQ'),
    #     ('tag_name_new1', 'etMoQQDQAA_Lca86F1dGKme-4qde0VJQ'),
    #     ('tag_name?', 'etMoQQDQAA_Lca86F1dGKme-4qde0VJQ'),
    # ])
    @pytest.mark.skip(reason='skip')
    def test_add_tag(self):
        # tag_name =tag_name+ str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        group_name="tmp123"
        tag=[{"name": uuid.uuid1()},
             {"name": uuid.uuid1()},
             {"name": uuid.uuid1()}]
        r=self.tag.add(group_name=group_name,tag=tag)
        assert r.status_code==200 and r['errcode']==0

    #添加全新标签
    def test_add_and_detect(self):
        # tag_name =tag_name+ str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        group_name="tmp123"
        tag=[{"name": '11'},
             {"name": "tag2"},
             {"name": "tag31"}]
        r=self.tag.add_and_detect(group_name=group_name,tag=tag)
        assert r

    #像指定组下添加标签
    def test_add_group_assign_tag(self):
        group_name="tmp123"
        tag_first=[{"name": '11'},
             {"name": "tag"},
             {"name": "tag31"}]
        tag_second=[{"name": self.tag.generate_unique_tag_name('tag')},
                    {"name": self.tag.generate_unique_tag_name('tag1')}]
        self.tag.add_and_detect(group_name=group_name,tag=tag_first)
        r=self.tag.add(group_name,tag_second)

    #删除标签
    # @pytest.mark.parametrize("tag_id",[
    #     'etMoQQDQAABbwEJAbIhNRu87l489sYEw',
    #     'etMoQQDQAAlFY29_c-nlNHLZzsFPzKBQ',
    #     # 'etMoQQDQAAIbsqLILajxZnuqQTI3XpEg'
    # ])

    # @pytest.mark.skip(reason='skip')
    def test_group_delete(self):
        r=self.tag.delete_group(group_id=['etMoQQDQAAvErLVWDNoKOff6o-44wkE'])
        # r=self.tag.list()
        # print(jsonpath(r.json(),f"$..[?(@.id=='etMoQQDQAAq6lttsvB49lm2bnXI-5TTQ')]"))
        # assert not (jsonpath(r.json(),f"$..[?(@.id=={tag_id})]"))



    # @pytest.mark.skip(reason='skip')
    def test_tag_delete(self):
        r=self.tag.delete_tag(tag_id=['etMoQQDQAACquqZ5jT9KwvfE10T46GY'])

    #删除标签
    def test_delete_and_detect_tag(self):
        r = self.tag.delete_and_detect_tag(['etMoQQDQAAMQNKuk9x7YwJszGijAXlZw'])
        assert r.json()['errcode'] == 0