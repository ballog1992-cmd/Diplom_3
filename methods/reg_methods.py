import allure
from methods.base_page import BasePageMethods
from locators import Locators
from curl import Url
from data import *


class UserAvtorization(BasePageMethods):

    def __init__(self, driver):
        super().__init__(driver) 
    
    @allure.step("Регистрация и вход пользователя")
    def register_and_login_user(self, name, email, password):
        self.click_to_element(Locators.PROFILE_LINK)
        self.click_to_element(Locators.REGISTER_LINK)
        self.driver.find_element(*Locators.NAME_INPUT_REG).send_keys(name)
        self.driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(password)
        self.click_to_element(Locators.REGISTER_BUTTON)
        
        self.wait_for_order_feed_url(Url.login_page)
        self.driver.find_element(*Locators.EMAIL_INPUT_LOG).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT_LOG).send_keys(password)
        self.click_to_element(Locators.LOGIN_BUTTON)
        self.wait_for_order_feed_url(Url.main_site)



