from frame1.main import Main


class TestMain:
    def test_main(self):
        main = Main().goto_market().goto_search().search()