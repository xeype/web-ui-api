from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class AllProductsPageLocators:
    LOCATOR_ALL_PRODUCTS = (By.XPATH, "//span[@class ='goods-tile__title']")


class AllProductsPageHelper(BasePage):
    def get_all_products_list(self):
        all_products = self.find_elements(AllProductsPageLocators.LOCATOR_ALL_PRODUCTS, time=5)
        products = [x.text for x in all_products if len(x.text) > 0]
        return products

    def get_all_product_items(self):
        all_product_items = self.find_elements(AllProductsPageLocators.LOCATOR_ALL_PRODUCTS, time=5)
        return all_product_items
