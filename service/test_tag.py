#coding:utf-8
import datetime
import pytest
from jsonpath import jsonpath
from service.tag import Tag

class TestTag:
    def setup_class(self):
        self.tag = Tag()
        r = self.tag.list()
        self.tag_id_origion = jsonpath(r.json(), "$..id")
        self.tag_name_origion = jsonpath(r.json(), "$..name")

    #数据清理
    def teardown_class(self):
        r=self.tag.list()
        tag_id_later = jsonpath(r.json(), "$..id")
        tag_id_later = jsonpath(r.json(), "$..name")
        for tag_id in tag_id_later:
            if tag_id not in self.tag_id_origion:
                self.tag.delete(tag_id)
        for tag_name in self.tag_name_origion:
            if tag_name not in tag_id_later:
                self.tag.add(tag_name)

    #更新标签
    @pytest.mark.parametrize("tag_id,tag_name",[
        ('etMoQQDQAAu47atKWLSSXFVYmy8doqiA', 'tag1_new_'),
        ('etMoQQDQAAu47atKWLSSXFVYmy8doqiA', 'tag1_中文'),
        ('etMoQQDQAAu47atKWLSSXFVYmy8doqiA', 'tag1_[中文]')
    ])
    def test_tag_update(self,tag_id,tag_name):
        # group_name='python15'
        # tag_id='etMoQQDQAACzSou6IVZVyDf33-zSC3ZQ'
        tag_name=tag_name+str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

        # r=self.tag.list()
        r=self.tag.update(id=tag_id,
                     tag_name=tag_name)
        r=self.tag.list()
        print(type(jsonpath(r.json(),f"$..[?(@.name=='{tag_name}')]")))
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
        # tags=[tag
        #       for group in r.json()['tag_group'] if group['group_name'] == group_name
        #       for tag in group['tag'] if tag['name'] == tag_name
        #       ]
        # assert tags !=[]

    #增加标签
    @pytest.mark.parametrize("tag_name,group_id",[
        ('tag_name中文', 'etMoQQDQAAhcpQCLYDCGfuLaTPQ1hQ5g'),
        ('tag_name_new1', 'etMoQQDQAAhcpQCLYDCGfuLaTPQ1hQ5g'),
        ('tag_name?', 'etMoQQDQAAhcpQCLYDCGfuLaTPQ1hQ5g'),
    ])
    def test_tag_add(self,tag_name,group_id):
        tag_name =tag_name+ str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        r=self.tag.add(tag_name,group_id)
        r=self.tag.list()
        assert jsonpath(r.json(),f"$..[?(@.name=='{tag_name}')]")[0]['name']==tag_name

    #删除标签
    @pytest.mark.parametrize("tag_id",[
        'etMoQQDQAAWTJ46mPoSlEiQp_mGeXxTQ',
        'etMoQQDQAAu47atKWLSSXFVYmy8doqiA',
        'etMoQQDQAAJn8o0ClcHL-YydtHc2xHKw'
    ])
    def test_tag_delete(self,tag_id):
        r=self.tag.delete(tag_id)
        r=self.tag.list()
        print(jsonpath(r.json(),f"$..[?(@.id=='etMoQQDQAAq6lttsvB49lm2bnXI-5TTQ')]"))
        assert not (jsonpath(r.json(),f"$..[?(@.id=={tag_id})]"))