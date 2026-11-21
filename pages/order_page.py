import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Получение счётчика «Выполнено за всё время»")
    def get_all_order_counter(self):
        element = self.wait_for_element_visible(OrderPageLocators.ALL_ORDER_COUNTER)
        return int(element.text.replace(" ", ""))

    @allure.step("Получение счётчика «Выполнено за сегодня»")
    def get_today_order_counter(self):
        element = self.wait_for_element_visible(OrderPageLocators.TODAY_ORDER_COUNTER)
        return int(element.text.replace(" ", ""))

    @allure.step("Получение списка заказов в разделе «В работе»")
    def get_in_progress_orders(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(OrderPageLocators.NUMBER_IN_PROGRESS_FIELD)
        )
        return [el.text.strip() for el in elements if el.text.strip().isdigit()]