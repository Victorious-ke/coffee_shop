# Coffee Shop

A simple Python project for modeling a coffee shop, customers, coffees, and orders.  
This project demonstrates relationships between classes (`Customer`, `Coffee`, `Order`) and includes validation logic with automated tests.

---

##  Project Structure
coffee_shop/
│── coffee.py # Coffee class
│── customer.py # Customer class
│── order.py # Order class
│── tests/ # Pytest test cases
│ ├── test_coffee.py
│ ├── test_customer.py
│ └── test_order.py




##  Features

- **Customer**
  - Create and manage coffee orders
  - Name validation (must be 2–15 characters, string only)

- **Coffee**
  - Name validation (3–20 characters, string only)
  - Track all orders for a coffee
  - Compute average price of orders

- **Order**
  - Connects a customer to a coffee with a price
  - Validates that price is a positive number

---

##  Running Tests

This project uses **pytest** for testing.

Run all tests with:

```bash
pytest




