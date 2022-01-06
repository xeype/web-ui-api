from ui.pages.main_page import SearchHelper
from ui.pages.all_products_page import ProductPageHelper
import pytest


@pytest.mark.parametrize('product', ['ВИНО', 'сыр', 'Пиво'])
def test_search(browser, product):
    main_rozetka = SearchHelper(browser)
    products_page = ProductPageHelper(browser)

    main_rozetka.go_to_site()
    main_rozetka.enter_word(product)
    main_rozetka.click_on_the_search_button()

    all_products = products_page.get_all_products()
    assert product.lower() in str(all_products).lower()
