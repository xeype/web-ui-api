from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class BasketPageLocators:
    LOCATOR_BASKET_TITLE = (By.XPATH, "//h3[@class='modal__heading']")
    LOCATOR_BASKET_PRODUCT_LIST = (By.XPATH, "//a[@class='cart-product__title']")


class BasketPageHelper(BasePage):
    def get_basket_title(self):
        title = self.find_element(BasketPageLocators.LOCATOR_BASKET_TITLE, time=5).text
        return title

    def get_basket_products_list(self):
        products = self.find_elements(BasketPageLocators.LOCATOR_BASKET_PRODUCT_LIST, time=5)
        products_list = [x.text for x in products if len(x.text) > 0]
        return products_list
