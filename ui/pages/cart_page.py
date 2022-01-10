from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class CartPageLocators:
    LOCATOR_CART_TITLE = (By.XPATH, "//h3[@class='modal__heading']")
    LOCATOR_CART_PRODUCT_LIST = (By.XPATH, "//a[@class='cart-product__title']")
    LOCATOR_EMPTY_CART_TITLE = (By.XPATH, "//h4[@class='cart-dummy__heading']")


class CartPageHelper(BasePage):
    def get_cart_title(self):
        title = self.find_element(CartPageLocators.LOCATOR_CART_TITLE, time=5).text
        return title

    def get_cart_products_list(self):
        products = self.find_elements(CartPageLocators.LOCATOR_CART_PRODUCT_LIST, time=5)
        products_list = [x.text for x in products if len(x.text) > 0]
        return products_list

    def get_empty_cart_title(self):
        title = self.find_element(CartPageLocators.LOCATOR_EMPTY_CART_TITLE, time=5).text
        return title
