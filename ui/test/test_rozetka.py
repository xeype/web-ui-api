import allure
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.main_page import MainPageHelper
from ui.pages.all_products_page import AllProductsPageHelper
from ui.pages.product_page import ProductPageHelper
from ui.pages.cart_page import CartPageHelper
import pytest
from selenium.webdriver.support import expected_conditions as EC

from ui.test.conftest import default_redirect_categories


@allure.title('Check cart is empty')
def test_check_cart_is_empty_by_default(browser):
    main_rozetka = MainPageHelper(browser)
    cart_page = CartPageHelper(browser)

    main_rozetka.go_to_site()
    main_rozetka.click_on_the_cart_icon()

    assert cart_page.get_empty_cart_title() == 'Корзина пуста'


@allure.title("Find product by search field")
@allure.description('Find product and verify that he present')
@pytest.mark.parametrize('product', ['ВИНО', 'сыр', 'Пиво'])
def test_find_product(browser, product):
    main_rozetka = MainPageHelper(browser)
    products_page = AllProductsPageHelper(browser)

    main_rozetka.go_to_site()
    main_rozetka.enter_word(product)
    main_rozetka.click_on_the_search_button()

    all_products = products_page.get_all_products_list()
    assert product.lower() in str(all_products).lower()


@allure.title('Cart pop up showed')
@allure.title('Add product and verify that cart pop up is showed')
@pytest.mark.parametrize('product', ['чай', 'Кофе'])
def test_cart_pop_up_is_showed_after_add_product(browser, product):
    main_rozetka = MainPageHelper(browser)
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


@allure.title('Search by categories')
@pytest.mark.parametrize('category', ['автотовары', 'книги', 'смартфон'])
def test_go_to_products_page_by_categories(browser, category):
    main_rozetka = MainPageHelper(browser)
    products_page = AllProductsPageHelper(browser)

    browser.maximize_window()

    main_rozetka.go_to_site()
    main_rozetka.click_on_the_category_by_name(category)

    category_title = products_page.get_category_name()

    assert category.lower() in category_title.lower()


@allure.title('Redirect to order page')
@allure.description('Add product to cart > Confirm buy > Wait to order page')
@pytest.mark.parametrize('product', ['чай'])
def test_redirect_to_order_page_after_confirm_buy(browser, product):
    main_rozetka = MainPageHelper(browser)
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

    assert product_title.lower() in str(cart_product_list).lower()

    cart_page.place_an_order()

    assert cart_page.get_order_title() == 'Оформление заказа'


@allure.title('All categories are clickable')
@allure.description('All categories must be clickable and redirect to the right pages')
@pytest.mark.parametrize('category', default_redirect_categories)
def test_all_categories_are_clickable_and_redirect_to_the_right_page(browser, category):
    main_rozetka = MainPageHelper(browser)
    products_page = AllProductsPageHelper(browser)
    browser.maximize_window()

    main_rozetka.go_to_site()
    main_rozetka.click_on_the_category_by_name(category)
    assert category.lower()[0] in products_page.get_category_name().lower()


@allure.title('Tours category are clickable')
@allure.description('Tours category must be clickable and redirect to the right pages')
@pytest.mark.parametrize('tour_category', ['Туры и отдых'])
def test_tours_category_are_clickable_and_redirect_to_the_right_page(browser, tour_category):
    main_rozetka = MainPageHelper(browser)
    browser.maximize_window()

    main_rozetka.go_to_site()
    main_rozetka.click_on_the_category_by_name(tour_category)
    assert 'rozetka.travel' in browser.current_url


@allure.title('Clothes category are clickable')
@allure.description('Clothes category must be clickable and redirect to the right pages')
@pytest.mark.parametrize('clothes_category', ['Одежда, обувь и украшения'])
def test_clothes_category_are_clickable_and_redirect_to_the_right_page(browser, clothes_category):
    main_rozetka = MainPageHelper(browser)
    browser.maximize_window()

    main_rozetka.go_to_site()
    main_rozetka.click_on_the_category_by_name(clothes_category)
    WebDriverWait(browser, 10).until(EC.url_contains('/shoes_clothes/'))
    assert '/shoes_clothes/' in browser.current_url


@allure.title('Promotions category are clickable')
@allure.description('Promotions category must be clickable and redirect to the right pages')
@pytest.mark.parametrize('promotions_category', ['Акции'])
def test_promotions_category_are_clickable_and_redirect_to_the_right_page(browser, promotions_category):
    main_rozetka = MainPageHelper(browser)
    browser.maximize_window()

    main_rozetka.go_to_site()
    main_rozetka.click_on_the_category_by_name(promotions_category)
    assert '/promotions/' in browser.current_url
