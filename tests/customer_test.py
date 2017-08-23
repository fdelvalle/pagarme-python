from pagarme import customer
from tests.resources.dictionaries import customer_dictionary


def test_create_customer():
    _customer = customer.create(customer_dictionary.CUSTOMER)
    assert _customer['id'] is not None


def test_find_all_customers():
    all_customers = customer.find_all()
    assert all_customers is not None


def test_find_by():
    _customer = customer.create(customer_dictionary.CUSTOMER)
    find_customer = customer.find_by(_customer['id'])
    assert _customer['id'] == find_customer['id']
