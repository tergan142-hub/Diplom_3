import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.login_page_locators import LoginLocators


class LoginPage(BasePage):

    @allure.step("Ввод email: {email}")
    def fill_email(self, email):
        element = self.wait.until(
            EC.element_to_be_clickable(LoginLocators.EMAIL_FIELD)
        )
        element.clear()
        element.send_keys(email)

    @allure.step("Ввод пароля")
    def fill_password(self, password):
        element = self.wait.until(
            EC.element_to_be_clickable(LoginLocators.PASSWORD_FIELD)
        )
        element.clear()
        element.send_keys(password)

    @allure.step("Вход в аккаунт: {email}")
    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_element(LoginLocators.LOGIN_BUTTON)