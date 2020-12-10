from service.contact import Contact


class TestContact:
    def setup(self):
        self.contact=Contact()

    #创建成员
    def test_create_member(self):
        r=self.contact.create_member_detect('wangwu','王五','13800000001',[1])
        assert r.status_code==200 and r.json()['errcode']==0
        r=self.contact.get_member('wangwu')
        assert r.json()['userid']=='wangwu'

    def test_get_member(self):
        r=self.contact.get_member_detect('name')
        assert r.json()['errcode']==0

    def test_delete_member(self):
        user_id='wangw'
        r=self.contact.delete_member_detect(user_id)
        assert r.status_code==200 and r.json()['errcode']==0
        r=self.contact.get_member(user_id)
        assert 'userid not found' in r.json()['errmsg']
