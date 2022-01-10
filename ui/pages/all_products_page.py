from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class AllProductsPageLocators:
    LOCATOR_ALL_PRODUCTS = (By.XPATH, "//span[@class ='goods-tile__title']")
    LOCATOR_PRODUCTS_TITLE = (By.XPATH, "//h1[@class='portal__heading ng-star-inserted']")


class AllProductsPageHelper(BasePage):
    def get_all_products_list(self):
        all_products = self.find_elements(AllProductsPageLocators.LOCATOR_ALL_PRODUCTS, time=5)
        products = [x.text for x in all_products if len(x.text) > 0]
        return products

    def get_all_product_items(self):
        all_product_items = self.find_elements(AllProductsPageLocators.LOCATOR_ALL_PRODUCTS, time=10)
        return all_product_items

    def get_category_name(self):
        category = self.find_element(AllProductsPageLocators.LOCATOR_PRODUCTS_TITLE, time=5).text
        return category
