import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_order_validation():
    c = Customer("Dana")
    coffee = Coffee("FlatWhite")

    # valid
    order = Order(c, coffee, 4.5)
    assert order.price == 4.5

    # invalid price
    with pytest.raises(Exception):
        Order(c, coffee, 0.5)
    with pytest.raises(Exception):
        Order(c, coffee, 12)

    # price immutability
    with pytest.raises(Exception):
        order.price = 9
