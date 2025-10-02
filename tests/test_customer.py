import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_customer_name_validation():
    c = Customer("Alice")
    assert c.name == "Alice"

    c.name = "Bob"
    assert c.name == "Bob"

    with pytest.raises(Exception):
        Customer("")
    with pytest.raises(Exception):
        Customer("ThisNameIsWayTooLong")
    with pytest.raises(Exception):
        Customer(123)

def test_customer_create_order_and_relationships():
    c = Customer("Charlie")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 5.0)

    assert order in c.orders()
    assert coffee in c.coffees()
