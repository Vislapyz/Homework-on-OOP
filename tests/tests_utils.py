import pytest
from src.utils import Category, Product


@pytest.fixture
def category_tv():
    return Category('Телевизор', 'Современные телевизоры', ['LG', 'Xiaomi', 'Samsung'])


def test_init(category_tv):
    assert category_tv.title == 'Телевизор'
    assert category_tv.description == 'Современные телевизоры'
    assert category_tv.products == None#['LG', 'Xiaomi', 'Samsung']
    assert Category.total_categories == 1
    assert Category.total_unique_products == 1



@pytest.fixture
def product_xiaomi():
    return Product('Xiaomi TV2', 'Телевизор 32, смарт ТВ', '16000.00', '3')


def test_init_product(product_xiaomi):
    assert product_xiaomi.title == 'Xiaomi TV2'
    assert product_xiaomi.description == 'Телевизор 32, смарт ТВ'
    assert product_xiaomi.price == '16000.00'
    assert product_xiaomi.in_stock == '3'