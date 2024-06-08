import pytest
from src.shop import Product, Shop

def test_product_creation():
    product = Product("Apple", 1.0, 10)
    assert product.name == "Apple"
    assert product.price == 1.0
    assert product.quantity == 10

def test_calculate_total_price():
    product = Product("Apple", 1.0, 10)
    assert product.calculate_total_price() == 10.0

def test_apply_discount():
    product = Product("Apple", 1.0, 10)
    product.apply_discount(0.1)
    assert product.price == 0.9
    with pytest.raises(ValueError):
        product.apply_discount(1.5)

def test_add_and_remove_product():
    shop = Shop()
    product = Product("Apple", 1.0, 10)
    shop.add_product(product)
    assert shop.find_product("Apple") == product
    shop.remove_product("Apple")
    assert shop.find_product("Apple") is None

def test_get_total_inventory_value():
    shop = Shop()
    product1 = Product("Apple", 1.0, 10)
    product2 = Product("Banana", 0.5, 20)
    shop.add_product(product1)
    shop.add_product(product2)
    assert shop.get_total_inventory_value() == 20.0

