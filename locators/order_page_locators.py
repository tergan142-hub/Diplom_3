import allure
from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_FEED_TITLE = [By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5' and text()='Лента заказов']"]

    ALL_ORDER_COUNTER = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]"]
    TODAY_ORDER_COUNTER = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]"]
    NUMBER_IN_PROGRESS_FIELD = [By.XPATH, "//p[text()='В работе:']/following-sibling::ul[contains(@class, 'OrderFeed_orderListReady')]/li"]