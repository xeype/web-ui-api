from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class ProductsPageLocators:
    LOCATOR_ALL_PRODUCTS = (By.XPATH, "//span[@class ='goods-tile__title']")


class ProductPageHelper(BasePage):
    def get_all_products(self):
        all_products = self.find_elements(ProductsPageLocators.LOCATOR_ALL_PRODUCTS, time=5)
        products = [x.text for x in all_products if len(x.text) > 0]
        return products
