from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object para a página do carrinho."""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    BTN_CHECKOUT = (By.ID, "checkout")
    BTN_CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def is_on_cart_page(self):
        return "cart" in self.get_url()

    def get_product_names(self):
        items = self.driver.find_elements(*self.ITEM_NAME)
        return [item.text for item in items]

    def has_product(self, product_name):
        return product_name in self.get_product_names()

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def is_cart_empty(self):
        return self.get_item_count() == 0

    def go_to_checkout(self):
        self.click(self.BTN_CHECKOUT)
