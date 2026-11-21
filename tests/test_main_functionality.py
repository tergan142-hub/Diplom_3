import allure

from pages.home_page import HomePage


@allure.epic("Stellar Burgers")
@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.story("Навигация")
    @allure.title("Переход по клику на «Конструктор»")
    @allure.description(
        "Со страницы «Лента заказов» кликаем по «Конструктор» и проверяем возврат на главную."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_constructor(self, driver):
        home_page = HomePage(driver)

        home_page.click_order_feed_button()
        assert home_page.is_order_feed_title_visible(), "Не удалось открыть «Ленту заказов»"

        home_page.click_constructor_button()
        assert home_page.is_main_title_visible(), "Не удалось перейти в «Конструктор»"

    @allure.story("Навигация")
    @allure.title("Переход по клику на раздел «Лента заказов»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_order_feed(self, driver):
        home_page = HomePage(driver)

        home_page.click_order_feed_button()
        assert home_page.is_order_feed_title_visible(), "Не удалось открыть «Ленту заказов»"

    @allure.story("Всплывающее окно ингредиента")
    @allure.title("При клике на ингредиент появляется всплывающее окно с деталями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_opening_window_with_details(self, driver):
        home_page = HomePage(driver)

        home_page.click_on_ingredient()
        assert home_page.is_ingredient_details_visible(), "Окно с деталями ингредиента не появилось"

    @allure.story("Всплывающее окно ингредиента")
    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.severity(allure.severity_level.NORMAL)
    def test_closing_window_with_details(self, driver):
        home_page = HomePage(driver)

        home_page.click_on_ingredient()
        home_page.closing_window_with_details()
        assert home_page.is_main_title_visible(), "Окно с деталями не закрылось"

    @allure.story("Счётчик ингредиента")
    @allure.title("Счётчик ингредиента увеличивается при добавлении в заказ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_counter_increases(self, driver):
        home_page = HomePage(driver)

        counter_before = home_page.get_ingredient_counter()
        home_page.drag_ingredient_to_constructor_js()
        counter_after = home_page.get_ingredient_counter_after_drag()

        assert counter_after == counter_before + 2, (
            f"Счётчик ингредиента не увеличился: было {counter_before}, стало {counter_after}"
        )