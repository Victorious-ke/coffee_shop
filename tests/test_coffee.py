import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_coffee_name_validation():
    with pytest.raises(Exception):
        Coffee("A")
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"
    with pytest.raises(Exception):
        coffee.name = "Cappuccino"

def test_coffee_orders_and_average():
    c1, c2 = Customer("Amy"), Customer("Ben")
    coffee = Coffee("Espresso")
    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 7.0)

    assert coffee.num_orders() == 2
    assert round(coffee.average_price(), 1) == 5.0
    assert c1 in coffee.customers()
    assert c2 in coffee.customers()
