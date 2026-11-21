import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import URLs
from locators.base_page_locators import BasePageLocators


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(URLs.BASE_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BasePageLocators.CONSTRUCTOR_BUTTON))

    allure.dynamic.parameter("browser", browser_name)

    yield driver
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """При падении теста прикрепляет скриншот к Allure-отчёту."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG,
            )

@pytest.fixture
def login_credentials():
    return {"email": "rejim@yandex.ru", "password": "Rejim123"}