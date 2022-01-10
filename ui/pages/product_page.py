from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class ProductPageLocators:
    LOCATOR_BUY_BUTTONS = (By.XPATH, "//app-buy-button")
    LOCATOR_PRODUCT_TITLE = (By.CLASS_NAME, 'product__title')


class ProductPageHelper(BasePage):
    def add_product_to_cart(self):
        buy_button = self.find_elements(ProductPageLocators.LOCATOR_BUY_BUTTONS, time=5)
        buy_button[0].click()

    def get_product_title(self):
        title = self.find_element(ProductPageLocators.LOCATOR_PRODUCT_TITLE, time=5).text
        return title
