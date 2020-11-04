from app.page.app import App

class TestContact:

    def setup(self):
        self.app=App()
        self.main=self.app.start().goto_main()

    def test_addcontact(self):
        name = 'name12'
        gender = '女'
        phoneNum = '13800011668'
        result=self.main.goto_address().click_addmember().add_member_menual().add_contact(name,gender,phoneNum).get_toast()
        assert '添加成功'==result

    def test_delete_member(self):
        name = '5677'
        delete = self.main.goto_address().goto_personal_info(name).goto_personal_info_setting().goto_edit_member().delete_member()
        assert True != delete.find_member(name)