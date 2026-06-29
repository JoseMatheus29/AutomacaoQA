from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object para as páginas de checkout (step one e step two)."""

    # Step One – Locators
    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_POSTAL_CODE = (By.ID, "postal-code")
    BTN_CONTINUE = (By.ID, "continue")
    MSG_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    # Step Two – Locators
    SUMMARY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    BTN_FINISH = (By.ID, "finish")

    # Confirmation – Locators
    SUCCESS_HEADER = (By.CLASS_NAME, "complete-header")
    SUCCESS_TEXT = (By.CLASS_NAME, "complete-text")
    PONY_EXPRESS = (By.CLASS_NAME, "pony_express")

    def fill_personal_info(self, first_name, last_name, postal_code):
        self.type(self.INPUT_FIRST_NAME, first_name)
        self.type(self.INPUT_LAST_NAME, last_name)
        self.type(self.INPUT_POSTAL_CODE, postal_code)
        self.click(self.BTN_CONTINUE)

    def get_error_message(self):
        return self.get_text(self.MSG_ERROR)

    def has_error(self):
        return self.is_visible(self.MSG_ERROR)

    def get_summary_items(self):
        items = self.driver.find_elements(*self.SUMMARY_ITEM_NAME)
        return [item.text for item in items]

    def finish_purchase(self):
        self.click(self.BTN_FINISH)

    def get_success_header(self):
        return self.get_text(self.SUCCESS_HEADER)

    def get_success_text(self):
        return self.get_text(self.SUCCESS_TEXT)

    def is_purchase_complete(self):
        return self.is_visible(self.SUCCESS_HEADER)
