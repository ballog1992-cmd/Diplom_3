from selenium.webdriver.common.by import By

class Locators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//header//p[text()='Конструктор']")
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")

    ALL_INGREDIENTS = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")

    MODAL_INGREDIENTS = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 button.Modal_modal__close__TnseK")
    LOADING_ANIMATION = (By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")
    CONTEINER_BUN = (By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, ".BurgerConstructor_basket__totalContainer__2Z-ho p")
    TOTAL_COUNTER = (By.CSS_SELECTOR, ".BurgerConstructor_basket__totalContainer__2Z-ho .text_type_digits-medium")

    PROFILE_LINK = (By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX:nth-child(3)")
    REGISTER_LINK = (By.CSS_SELECTOR, "p.text_type_main-default:nth-child(1) > a:nth-child(1)")


    NAME_INPUT_REG = (By.XPATH, "//div[contains(@class, 'input') and .//label[text()='Имя']]//input")
    EMAIL_INPUT_REG = (By.CSS_SELECTOR, "fieldset:nth-child(2) input[type='text']")
    PASSWORD_INPUT_REG = (By.CSS_SELECTOR, "fieldset:nth-child(3) input[type='password']")

    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    EMAIL_INPUT_LOG = (By.CSS_SELECTOR, ".input_type_text > input:nth-child(2)")
    PASSWORD_INPUT_LOG = (By.CSS_SELECTOR, ".input_type_password > input:nth-child(2)")

    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0")

    ACCOUNT_BUTTON_EXIT = (By.XPATH, "//nav[contains(@class, 'Account_nav')]//button")
    
    ORDER_BUTTON = (By.XPATH, "//button[contains(., 'Оформить заказ')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2")
    FIRST_ORDER = (By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r:first-child p.text_type_digits-default")
    NAMBER_IN_PROGRESS = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem > li:nth-child(1)")
    NAMBER_IN_COMPLITED_ALL_TIME = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    NAMBER_IN_COMPLITED_TODAY = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
