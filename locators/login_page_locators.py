import allure
from selenium.webdriver.common.by import By

class LoginLocators:

    EMAIL_FIELD = [By.XPATH, "//input[@name='name']"]
    PASSWORD_FIELD = [By.XPATH, "//input[@name='Пароль']"]
    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"]