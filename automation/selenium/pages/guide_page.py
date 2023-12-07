from selenium.webdriver.common.by import By
from .base_page import BasePage

class GuidePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.title_locator = (By.XPATH, "//h1[text()='Guide']")
        self.subtitles = [
            "Getting a resource",
            "Listing all resources",
            "Creating a resource",
            "Updating a resource",
            "Patching a resource",
            "Deleting a resource",
            "Filtering resources",
            "Listing nested resources"
        ]

    def verify_guide_page_elements(self):
        self.wait_for_element(*self.title_locator)
        for subtitle in self.subtitles:
            subtitle_locator = (By.XPATH, f"//h2[text()='{subtitle}']")
            self.wait_for_element(*subtitle_locator)
