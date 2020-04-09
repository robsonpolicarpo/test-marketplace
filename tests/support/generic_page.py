from selene.api import s


class GenericPage(object):
    TIMEOUT_DEFAULT = 15

    def __init__(self, driver):
        self.driver = driver

    def get_elem_by_text(self, text):
        return s(f"//*[text()='{text}']")

    def get_element_by_contains_text(self, text):
        return s(f"//*[contains(text(), '{text}')]")

    def focus(self, element):
        self.driver.driver.execute_script("arguments[0].scrollIntoView();", element)
