from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addMember1(self):
        username = 'aaaaj'
        accout = 'aaaaj'
        phoneNumber = '13900000011'
        addmember = self.main.goto_addMember()
        addmember.add_member(username, accout, phoneNumber)
        assert username in addmember.get_member(username)
