from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class MainPageLocators:
    LOCATOR_PRODUCT_SEARCH_FIELD = (By.NAME, "search")
    LOCATOR_SEARCH_BUTTON = (By.XPATH, "//header/div/div/div/form/button")
    LOCATOR_CART_ICON = (By.XPATH, '//rz-cart')
    LOCATOR_SIDEBAR_MENU = (By.XPATH, '//sidebar-fat-menu/div/ul/li')


class MainPageHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(MainPageLocators.LOCATOR_PRODUCT_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(MainPageLocators.LOCATOR_SEARCH_BUTTON, time=5).click()

    def click_on_the_cart_icon(self):
        return self.find_element(MainPageLocators.LOCATOR_CART_ICON, time=5).click()

    def click_on_the_category_by_name(self, category_name):
        categories_list = self.find_elements(MainPageLocators.LOCATOR_SIDEBAR_MENU)
        for category in categories_list:
            if category_name.lower() in category.text.lower():
                return category.click()

    def get_all_categories(self):
        return self.find_elements(MainPageLocators.LOCATOR_SIDEBAR_MENU)
