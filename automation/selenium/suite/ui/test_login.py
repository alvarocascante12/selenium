import allure
import pytest
from automation.selenium.pages.home_page import HomePage
from automation.selenium.pages.guide_page import GuidePage
from automation.selenium.pages.webdriver_factory import WebDriverFactory


@allure.feature("UI Tests")
@allure.title("Guide Link Navigation Test")
class TestGuideLinkNavigation:
    @pytest.fixture(scope="function")
    def setup(request):
        driver = WebDriverFactory.get_driver()
        yield driver
        WebDriverFactory.quit_driver()

    @allure.story("Navigate to Guide Page")
    def test_guide_link_navigation(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.open_url(home_page.base_url)
        home_page.navigate_to_guide_page()

        guide_page = GuidePage(driver)
        guide_page.verify_guide_page_elements()
