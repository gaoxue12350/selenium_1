from frame1.base_page import BasePage


class Search(BasePage):
    def search(self):
        self.parse_yaml("./search.yaml","search")
        return True