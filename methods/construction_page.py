import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from methods.reg_methods import UserAvtorization
from locators import Locators
from curl import Url
from data import *



class IngPageMethods(UserAvtorization):

    
    @allure.step("Перейти на страницу ленты заказов")
    def go_to_order_feed(self):
        self.click_to_element(Locators.ORDER_FEED)
        self.wait_for_order_feed_url(Url.order_page)

    @allure.step("Перейти на главную страницу")
    def constructor_page(self):
        self.click_to_element(Locators.CONSTRUCTOR_BUTTON)
        self.wait_for_order_feed_url(Url.main_site)

    @allure.step("Выбрать ингридиент по {ingr_id}")
    def add_ingredient_to_order_by_index(self, ingr_id):
        self.wait_for_element_visibility(Locators.ALL_INGREDIENTS)
        ingredients = self.driver.find_elements(*Locators.ALL_INGREDIENTS)
        return ingredients[ingr_id]
    
    @allure.step("Открыть модальное окно ингредиента и получить информацию о ингридиенте")
    def open_ingredient_details(self, ingredient_element):
        self.driver.execute_script("arguments[0].scrollIntoView();", ingredient_element)
        self.click_to_element(ingredient_element)
        return self.wait_for_element_visibility(Locators.MODAL_INGREDIENTS)

    @allure.step("Перетаскивание ингредиента в заказ (JS эмуляция)")
    def drag_and_drop_element(self, source, target):
        source_element = source if isinstance(source, WebElement) else self.driver.find_element(*source)
        target_element = target if isinstance(target, WebElement) else self.driver.find_element(*target)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source_element)

        js_script = """
        const source = arguments[0];
        const target = arguments[1];
        
        const dataTransfer = new DataTransfer();
        
        const dragStartEvent = new DragEvent('dragstart', {
            bubbles: true, cancelable: true, dataTransfer
        });
        source.dispatchEvent(dragStartEvent);
        
        const dropEvent = new DragEvent('drop', {
            bubbles: true, cancelable: true, dataTransfer
        });
        target.dispatchEvent(dropEvent);
        
        const dragEndEvent = new DragEvent('dragend', {
            bubbles: true, cancelable: true, dataTransfer
        });
        source.dispatchEvent(dragEndEvent);
        """

        self.driver.execute_script(js_script, source_element, target_element)


    @allure.step("Получить значение счетчика ингредиентов")
    def ingredient_counter_value(self):
        counter_element = self.wait_for_element_visibility(Locators.TOTAL_COUNTER)
        return int(counter_element)
    
    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):

        self.wait_for_modal_to_disappear()
        
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(Locators.ORDER_NUMBER, "9999")
        )
        
        element = self.driver.find_element(*Locators.ORDER_NUMBER)
        return element.text.strip()

    
    @allure.step("Получить текст номера заказа")
    def get_first_order_text_from_history(self):

        order_text = self.wait_for_element_visibility(Locators.NAMBER_IN_PROGRESS)

        return order_text.strip().replace('#', '')
    
    @allure.step("Получить значение счетчика 'Выполнено за все время'")
    def get_namber_all_time_complited(self):

        text_value = self.wait_for_element_visibility(Locators.NAMBER_IN_COMPLITED_ALL_TIME)

        return int(text_value)
    
    @allure.step("Получить значение счетчика 'Выполнено за сегодня")
    def get_namber_all_today_complited(self):

        text_value = self.wait_for_element_visibility(Locators.NAMBER_IN_COMPLITED_TODAY)

        return int(text_value)