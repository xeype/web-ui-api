import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


default_redirect_categories = ['Ноутбуки и компьютеры', 'Смартфоны, ТВ и электроника', 'Товары для геймеров',
                               'Бытовая техника', 'Товары для дома', 'Инструменты и автотовары',
                               'Сантехника и ремонт', 'Дача, сад и огород', 'Спорт и увлечения',
                               'Красота и здоровье', 'Детские товары',
                               'Зоотовары', 'Канцтовары и книги', 'Алкогольные напитки и продукты',
                               'Товары для бизнеса и услуги']


@pytest.fixture(params='default_redirect_categories')
def categories(request):
    return request.param
