import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators


class HomePage(BasePage):

    @allure.step("Клик по кнопке «Конструктор»")
    def click_constructor_button(self):
        self.click_element(BasePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по разделу «Лента заказов»")
    def click_order_feed_button(self):
        self.click_element(BasePageLocators.ORDER_FEED_BUTTON)

    @allure.step("Проверка видимости заголовка главной страницы")
    def is_main_title_visible(self):
        return self.wait_for_element_visible(BasePageLocators.MAIN_TITLE).is_displayed()

    @allure.step("Проверка видимости заголовка «Лента заказов»")
    def is_order_feed_title_visible(self):
        return self.wait_for_element_visible(OrderPageLocators.ORDER_FEED_TITLE).is_displayed()

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        return self.click_element(BasePageLocators.INGREDIENT)

    @allure.step("Проверка видимости окна с деталями ингредиента")
    def is_ingredient_details_visible(self):
        return self.wait_for_element_visible(BasePageLocators.INGREDIENT_DETAILS).is_displayed()

    @allure.step("Закрытие окна с деталями ингредиента")
    def closing_window_with_details(self):
        return self.click_element(BasePageLocators.CROSS_FOR_CLOSING)

    @allure.step("Получение значения счётчика ингредиента")
    def get_ingredient_counter(self):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(BasePageLocators.INGREDIENT_COUNTER)
            )
            return int(element.text)
        except TimeoutException:
            return 0

    @allure.step("Перетаскивание ингредиента в конструктор (ActionChains)")
    def drag_ingredient_to_constructor(self):
        source = self.wait.until(
            EC.visibility_of_element_located(BasePageLocators.INGREDIENT)
        )
        target = self.wait.until(
            EC.visibility_of_element_located(BasePageLocators.CONSTRUCTOR_BASKET)
        )
        ActionChains(self.driver).click_and_hold(source).move_to_element(target).release().perform()

    @allure.step("Получение счётчика ингредиента после перетаскивания")
    def get_ingredient_counter_after_drag(self):
        return self.get_ingredient_counter()

    @allure.step("Перетаскивание ингредиента в конструктор (JavaScript)")
    def drag_ingredient_to_constructor_js(self):
        source = self.wait.until(
            EC.presence_of_element_located(BasePageLocators.INGREDIENT)
        )
        target = self.wait.until(
            EC.presence_of_element_located(BasePageLocators.CONSTRUCTOR_BASKET)
        )

        js_script = """
        function simulateDragDrop(sourceNode, targetNode) {
            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { dataTransfer: dataTransfer, bubbles: true });
            sourceNode.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', { dataTransfer: dataTransfer, bubbles: true });
            targetNode.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', { dataTransfer: dataTransfer, bubbles: true });
            targetNode.dispatchEvent(dropEvent);
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_script, source, target)

    @allure.step("Клик по кнопке «Личный кабинет» / «Войти в аккаунт»")
    def click_on_personal_account_button(self):
        return self.click_element(BasePageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик по кнопке «Оформить заказ»")
    def click_checkout_button(self):
        self.click_element(BasePageLocators.PLACING_ORDER_BUTTON)

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number(self):
        self.wait.until(
            lambda d: d.find_element(*BasePageLocators.POPUP_NUMBER).text.strip() != "9999"
        )
        element = self.wait_for_element_visible(BasePageLocators.POPUP_NUMBER)
        return element.text.strip()

    @allure.step("Закрытие модального окна с номером заказа")
    def close_order_popup(self):
        self.click_element_js(BasePageLocators.POPUP_ORDER_CROSS)
        self.wait.until(EC.invisibility_of_element_located(BasePageLocators.POPUP_WINDOW))