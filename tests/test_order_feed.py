import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
from data_generators import normalize_order_number


@allure.epic("Stellar Burgers")
@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.story("Счётчики заказов")
    @allure.title("Счётчик «Выполнено за всё время» увеличивается после заказа")
    @allure.description(
        "Запоминаем счётчик «Выполнено за всё время» в ленте, логинимся, "
        "оформляем заказ и проверяем, что счётчик увеличился на 1."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_total_order_count_increases(self, driver, login_credentials):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        home_page.click_order_feed_button()
        counter_before = order_page.get_all_order_counter()

        home_page.click_constructor_button()
        home_page.click_on_personal_account_button()
        login_page.login(login_credentials["email"], login_credentials["password"])

        home_page.drag_ingredient_to_constructor_js()
        home_page.click_checkout_button()

        order_number = home_page.get_order_number()
        home_page.close_order_popup()
        home_page.click_order_feed_button()

        counter_after = order_page.get_all_order_counter()

        assert counter_after == counter_before + 1, (
            f"Счётчик «Выполнено за всё время» не увеличился: "
            f"было {counter_before}, стало {counter_after} (заказ №{order_number})"
        )

    @allure.story("Счётчики заказов")
    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после заказа")
    @allure.description(
        "Запоминаем счётчик «Выполнено за сегодня» в ленте, логинимся, "
        "оформляем заказ и проверяем, что счётчик увеличился на 1."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_today_order_count_increases(self, driver, login_credentials):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        home_page.click_order_feed_button()
        counter_before = order_page.get_today_order_counter()

        home_page.click_constructor_button()
        home_page.click_on_personal_account_button()
        login_page.login(login_credentials["email"], login_credentials["password"])

        home_page.drag_ingredient_to_constructor_js()
        home_page.click_checkout_button()

        order_number = home_page.get_order_number()
        home_page.close_order_popup()
        home_page.click_order_feed_button()

        counter_after = order_page.get_today_order_counter()

        assert counter_after == counter_before + 1, (
            f"Счётчик «Выполнено за сегодня» не увеличился: "
            f"было {counter_before}, стало {counter_after} (заказ №{order_number})"
        )

    @allure.story("Заказы в работе")
    @allure.title("Номер оформленного заказа появляется в разделе «В работе»")
    @allure.description(
        "Оформляем заказ, запоминаем его номер и проверяем, что он появился "
        "в списке заказов раздела «В работе» (с учётом ведущих нулей)."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_number_appears_in_progress(self, driver, login_credentials):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        home_page.click_on_personal_account_button()
        login_page.login(login_credentials["email"], login_credentials["password"])

        home_page.drag_ingredient_to_constructor_js()
        home_page.click_checkout_button()

        order_number = home_page.get_order_number()
        home_page.close_order_popup()
        home_page.click_order_feed_button()

        in_progress_orders = order_page.get_in_progress_orders()

        normalized_order_number = normalize_order_number(order_number)
        normalized_in_progress = [normalize_order_number(n) for n in in_progress_orders]

        assert normalized_order_number in normalized_in_progress, (
            f"Номер заказа {order_number} не найден в разделе «В работе». "
            f"В работе: {in_progress_orders}"
        )