from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from automation.selenium.settings.common import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL
        self.timeout = 10

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, by, value):
        try:
            element_present = EC.presence_of_element_located((by, value))
            WebDriverWait(self.driver, self.timeout).until(element_present)
        except TimeoutException:
            print(f"Element with {by}={value} not found within {self.timeout} seconds")

    def click_element(self, by, value):
        self.wait_for_element(by, value)
        self.driver.find_element(by, value).click()
