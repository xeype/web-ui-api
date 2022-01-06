from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class MainPageLocators:
    LOCATOR_PRODUCT_SEARCH_FIELD = (By.NAME, "search")
    LOCATOR_SEARCH_BUTTON = (By.XPATH, "//header/div/div/div/form/button")


class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(MainPageLocators.LOCATOR_PRODUCT_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(MainPageLocators.LOCATOR_SEARCH_BUTTON, time=5).click()
