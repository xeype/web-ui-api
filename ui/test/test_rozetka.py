from ui.pages.main_page import SearchHelper
from ui.pages.all_products_page import AllProductsPageHelper
from ui.pages.product_page import ProductPageHelper
from ui.pages.cart_page import CartPageHelper
import pytest


def test_check_cart_is_empty_by_default(browser):
    main_rozetka = SearchHelper(browser)
    cart_page = CartPageHelper(browser)

    main_rozetka.go_to_site()
    main_rozetka.click_on_the_cart_icon()

    assert cart_page.get_empty_cart_title() == 'Корзина пуста'


@pytest.mark.parametrize('product', ['ВИНО', 'сыр', 'Пиво'])
def test_find_product(browser, product):
    main_rozetka = SearchHelper(browser)
    products_page = AllProductsPageHelper(browser)

    main_rozetka.go_to_site()
    main_rozetka.enter_word(product)
    main_rozetka.click_on_the_search_button()

    all_products = products_page.get_all_products_list()
    assert product.lower() in str(all_products).lower()


@pytest.mark.parametrize('product', ['чай', 'Кофе'])
def test_cart_pop_up_is_showed_after_add_product(browser, product):
    main_rozetka = SearchHelper(browser)
    products_page = AllProductsPageHelper(browser)
    product_page = ProductPageHelper(browser)
    cart_page = CartPageHelper(browser)

    main_rozetka.go_to_site()
    main_rozetka.enter_word(product)
    main_rozetka.click_on_the_search_button()

    all_products = products_page.get_all_product_items()
    all_products[0].click()

    product_title = product_page.get_product_title()
    product_page.add_product_to_cart()

    cart_product_list = cart_page.get_cart_products_list()

    assert cart_page.get_cart_title() == 'Корзина'
    assert product_title.lower() in str(cart_product_list).lower()
