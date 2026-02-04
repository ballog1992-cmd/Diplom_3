import allure
import pytest
from methods.construction_page import IngPageMethods
from locators import Locators
from curl import Url
from data import *


class TestBaseFunctionally:

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_order_feed_success(self, driver):

        driver.get(Url.main_site)
        main_page = IngPageMethods(driver)
        
        main_page.go_to_order_feed()
        
        assert "feed" in driver.current_url

    @allure.title('Переход по клику на «Лента заказов» и обратно на «Конструктор»')
    def test_click_construction_success(self, driver):

        driver.get(Url.main_site)
        main_page = IngPageMethods(driver)
        
        main_page.go_to_order_feed()
        main_page.constructor_page()
        
        assert Url.main_site in driver.current_url

    @allure.title('Переход на всплывающее окно с деталями при клике на ингридиент с ID {ingr_id}')
    def test_click_ingredient_shows_modal_detals_ingridient(self, driver):

        driver.get(Url.main_site)
        main_page = IngPageMethods(driver)

        target_ingredient = main_page.add_ingredient_to_order_by_index(ingr_id)
        main_page.open_ingredient_details(target_ingredient)

        assert Url.modal_ingridient in driver.current_url

    @allure.title('Закрытие окна с деталями ингридента при клике на кнопку(крестик) закрытия окна')
    def test_close_ingredient_modal_on_button_click (self, driver):

        driver.get(Url.main_site)
        main_page = IngPageMethods(driver)

        target_ingredient = main_page.add_ingredient_to_order_by_index(ingr_id)
        main_page.open_ingredient_details(target_ingredient)
        main_page.click_with_js(Locators.CLOSE_BUTTON)

        assert Url.main_site in driver.current_url

    @allure.title('Перетаскивание ингридиентов в заказ')
    def test_drag_ingredient_to_basket(self, driver):

        driver.get(Url.main_site)
        main_page = IngPageMethods(driver) 

        target_ingredient = main_page.add_ingredient_to_order_by_index(ingr_id)
        main_page.drag_and_drop_element(target_ingredient, Locators.CONTEINER_BUN)
        count = main_page.ingredient_counter_value()

        assert count > 0

    @allure.title('Проверка открытия деталей ингредиента под авторизованным пользователем')
    def test_open_ingredient_modal_with_auth(self, driver, auth_user):

        page = auth_user 
        
    
        target_ingredient = page.add_ingredient_to_order_by_index(ingr_id)
        page.open_ingredient_details(target_ingredient)

        assert Url.modal_ingridient in driver.current_url

    @allure.title('Перетаскивание ингридиентов в заказ')
    @allure.description("После получения номера заказа локатор NAMBER_IN_PROGRESS захватывает текст 'Все текущие заказы готовы!' в место номера заказа")
    @pytest.mark.xfail(reason="При прогоне теста локатор NAMBER_IN_PROGRESS не успевает захватить номер заказа")
    def test_order_number_in_progress_new_order(self,auth_user):
        page = auth_user

        id_7 = page.add_ingredient_to_order_by_index(7)
        page.drag_and_drop_element(id_7, Locators.CONTEINER_BUN)

        id_1 = page.add_ingredient_to_order_by_index(1)
        page.drag_and_drop_element(id_1, Locators.CONTEINER_BUN)
        
        page.click_to_element(Locators.ORDER_BUTTON)
        order_number = page.get_order_number_from_modal()
        page.click_with_js(Locators.CLOSE_BUTTON)
        page.go_to_order_feed()
        
        history_order = page.get_first_order_text_from_history()
        assert order_number in history_order

    
    @allure.title("Проверяем увеличилось ли значение счетчика 'Выполнено за все время'")
    @allure.description("После регестрации и создании заказа в Firefox нельзя добавить ингридиенты")
    @pytest.mark.xfail(reason="При прогоне теста после регестрации и создании заказа в Firefox перестает работать метод drag_and_drop_element")
    def test_counter_completed_for_all_time_increases(self,auth_user):
        page = auth_user

        page.go_to_order_feed()
        history_order = page.get_namber_all_time_complited()
        page.constructor_page()

        id_7 = page.add_ingredient_to_order_by_index(7)
        page.drag_and_drop_element(id_7, Locators.CONTEINER_BUN)

        id_1 = page.add_ingredient_to_order_by_index(1)
        page.drag_and_drop_element(id_1, Locators.CONTEINER_BUN)

        page.click_to_element(Locators.ORDER_BUTTON)
        page.get_order_number_from_modal()

        page.click_with_js(Locators.CLOSE_BUTTON)
        page.go_to_order_feed()
        
        new_history = page.get_namber_all_time_complited()
        assert new_history > history_order

    @allure.title("Проверяем увеличилось ли значение счетчика 'Выполнено за сегодня'")
    @allure.description("После регестрации и создании заказа в Firefox нельзя добавить ингридиенты")
    @pytest.mark.xfail(reason="При прогоне теста после регестрации и создании заказа в Firefox перестает работать метод drag_and_drop_element")
    def test_counter_completed_for_all_today_increases(self,auth_user):
        page = auth_user

        page.go_to_order_feed()
        history_order = page.get_namber_all_today_complited()
        page.constructor_page()

        id_7 = page.add_ingredient_to_order_by_index(7)
        page.drag_and_drop_element(id_7, Locators.CONTEINER_BUN)

        id_1 = page.add_ingredient_to_order_by_index(1)
        page.drag_and_drop_element(id_1, Locators.CONTEINER_BUN)

        page.click_to_element(Locators.ORDER_BUTTON)
        page.get_order_number_from_modal()

        page.click_with_js(Locators.CLOSE_BUTTON)
        page.go_to_order_feed()
        
        new_history = page.get_namber_all_today_complited()
        assert new_history > history_order