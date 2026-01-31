import pytest
from selenium import webdriver
from methods.base_page import BasePageMethods
from locators import Locators
from curl import Url
from helper import generate_registration_data
from methods.reg_methods import UserAvtorization
from methods.construction_page import IngPageMethods
from selenium.webdriver.firefox.options import Options

class WebDriverFactory:
    @staticmethod
    def get_webdriver(browser_name):

        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported: {browser_name}")
    
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action= "store", default="chrome",help="Выбор браузера: 'chrome' или 'firefox'"

    )


@pytest.fixture
def driver(request):

    browser_name = request.config.getoption("--browser")

    driver = WebDriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def auth_user(driver):
    
    page = IngPageMethods(driver) 
    name, email, password = generate_registration_data()
    
    driver.get(Url.main_site)
    page.register_and_login_user(name, email, password)
    

    yield page 
    
    driver.get(Url.main_site) 
    
    page.click_to_element(Locators.PROFILE_LINK)
    page.wait_for_element_visibility(Locators.ACCOUNT_BUTTON_EXIT)
    page.click_to_element(Locators.ACCOUNT_BUTTON_EXIT)

