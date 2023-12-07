from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.guide_link = (By.LINK_TEXT, "Guide")

    def navigate_to_guide_page(self):
        self.click_element(*self.guide_link)
