from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object para a página de login do SauceDemo."""

    URL = "https://www.saucedemo.com/"

    # Locators
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")
    MSG_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type(self.INPUT_USERNAME, username)
        self.type(self.INPUT_PASSWORD, password)
        self.click(self.BTN_LOGIN)
        return self

    def get_error_message(self):
        return self.get_text(self.MSG_ERROR)

    def has_error(self):
        return self.is_visible(self.MSG_ERROR)
