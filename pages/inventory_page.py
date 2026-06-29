from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object para a página de produtos (inventory)."""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    # Primeiro produto da lista
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item:first-child .inventory_item_name")
    FIRST_PRODUCT_BTN_ADD = (By.CSS_SELECTOR, ".inventory_item:first-child button")

    def is_on_inventory_page(self):
        return "inventory" in self.get_url()

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_first_product_to_cart(self):
        name = self.get_text(self.FIRST_PRODUCT_NAME)
        self.click(self.FIRST_PRODUCT_BTN_ADD)
        return name  # retorna o nome do produto adicionado

    def get_cart_count(self):
        try:
            return self.get_text(self.CART_BADGE)
        except Exception:
            return "0"

    def go_to_cart(self):
        self.click(self.CART_ICON)
