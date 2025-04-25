from inventory_management import Inventory
import pytest


def test_add_stock():
    inventory = Inventory()
    inventory.add_stock("apple", 5)
    assert inventory.stock["apple"] == 5

def test_remove_stock():
    inventory = Inventory()
    inventory.add_stock("marker", 5)
    inventory.remove_stock("marker", 2)
    assert inventory.stock["marker"] == 3
    with pytest.raises(ValueError):
        inventory.remove_stock("shoe", 4)

def test_check_availability():
    inventory = Inventory()
    inventory.add_stock("orange", 1)
    assert inventory.check_availability("orange", 1) is True
    assert inventory.check_availability("orange", 2) is False

def test_remove_stock_with_insufficient_inventory():
    inventory = Inventory()
    with pytest.raises(ValueError):
        inventory.remove_stock("grape", 1)

def test_full_inventory_cycle():
    inventory = Inventory()
    inventory.add_stock("watermelon", 8)
    inventory.remove_stock("watermelon", 2)
    assert inventory.check_availability("watermelon", 6) is True
    inventory.remove_stock("watermelon", 6)
    assert inventory.check_availability("watermelon", 1) is False