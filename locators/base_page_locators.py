import allure
from selenium.webdriver.common.by import By

class BasePageLocators:
    CONSTRUCTOR_BUTTON = [By.XPATH,"//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"]
    ORDER_FEED_BUTTON = [By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']"]
    LOGO = [By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a[@href='/']"]

    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    INGREDIENT = [By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a"]   
    INGREDIENT_DETAILS = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    CROSS_FOR_CLOSING = [By.XPATH, "//div[contains(@class, 'Modal_modal__container')][.//h2[text()='Детали ингредиента']]//button[contains(@class, 'Modal_modal__close')]"]

    INGREDIENT_COUNTER = [By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a//p[contains(@class, 'counter')]"]
    CONSTRUCTOR_BASKET = [By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']"]

    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, "//button[text()='Войти в аккаунт']"]
    PLACING_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    POPUP_WINDOW = [By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']"]
    POPUP_ORDER_CROSS = [By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//button[contains(@class, 'Modal_modal__close_modified')]"]
    POPUP_NUMBER = [By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]//h2[contains(@class,'Modal_modal__title') and contains(@class,'text_type_digits-large')]"]