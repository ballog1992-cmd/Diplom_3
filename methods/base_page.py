import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class BasePageMethods:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.locators = Locators()
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Клик на элемент {locator}")
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.click_with_js(locator)

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
    
    @allure.step("Дождаться, что элемент {locator} станет кликабельным ")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Дождаться видимости экрана {url}")
    def wait_for_order_feed_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url))

    @allure.step("Дождаться закрытия модального окна")
    def wait_for_modal_to_disappear(self):

        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(Locators.LOADING_ANIMATION)
        )
    @allure.step("Принудительный клик через JS")
    def click_with_js(self, element_or_locator):
    
        if isinstance(element_or_locator, tuple):
            element_or_locator = self.driver.find_element(*element_or_locator)
        
        self.driver.execute_script("arguments[0].click();", element_or_locator)
