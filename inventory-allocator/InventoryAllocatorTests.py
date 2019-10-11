import unittest
import InventoryAllocator

class InventoryAllocatorTests(unittest.TestCase):
    """
        Unit testing for the InventoryAllocator.py class. This challenge was completed by
        Calvin Tang (calvintang@berkeley.edu) for the Deliverr coding challenge.

        To run these tests, please use the following command in your command line:
            python3 InventoryAllocatorTests.py

        If you have any questions about my implementation, experience, or application, please
        do not hesitate to reach out.
    """

    # Test for single match
    def test_exact_match(self):
        order, warehouses = { "apple": 1 }, [{ "name": "owd", "inventory": { "apple": 1 } }]
        expected = [{ "owd": { "apple": 1 } }]
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

    # Tests for empty warehouse inventory
    def test_not_enough_inventory(self):
        order, warehouses = { "apple": 1 }, [{ "name": "owd", "inventory": { "apple": 0 } }]
        expected = []
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

    # Tests for getting order items from different warehouses
    def test_split_warehouses(self):
        order, warehouses = { "apple": 10 }, [{ "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": 5 }}]
        expected = [{ "owd": { "apple": 5 }}, { "dm": { "apple": 5 } }]
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

    # Tests for empty inputs
    def test_empty_input(self):
        order, warehouses = {}, []
        expected = []
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

    # Tests if no warehouses have desired item
    def test_no_inventory(self):
        order, warehouses = { "banana": 10 }, [{ "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": 5 }}]
        expected = []
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

    # Tests if no warehouses have desired item
    def test_unknown_item(self):
        order, warehouses = { "apricot": 10 }, [{ "name": "owd", "inventory": { "apple": 5, "banana": 7 } }, { "name": "dm", "inventory": { "apple": 5, "banana": 5, "peach": 3, "cherry": 5 }}]
        expected = []
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

    # Tests longer input lists
    def test_long_request(self):
        order, warehouses = { "apple": 10, "banana": 10, "peach": 10, "cherry": 10 }, [{ "name": "owd", "inventory": { "apple": 5, "banana": 2 } }, { "name": "dm", "inventory": { "apple": 5, "banana": 5, "peach": 3, "cherry": 5 }}, {"name": "td", "inventory": {"apple": 14, "banana": 4, "peach": 7, "cherry": 5}}]
        expected = [{"owd": {"apple": 5, "banana": 2}}, {"dm": {"apple": 5, "banana": 5, "peach": 3, "cherry": 5}}, {"td": {"banana": 3, "peach": 7, "cherry": 5}}]
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

    # Tests for incorrect order values
    def test_negative_order(self):
        order, warehouses = { "apple": -1 }, [{ "name": "owd", "inventory": { "apple": 5 } }]
        expected = []
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

    # Tests for incorrect invetory values
    def test_negative_inventory(self):
        order, warehouses = { "apple": 3 }, [{ "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": -5, "banana": 5, "peach": 3, "cherry": 5 }}]
        expected = []
        self.assertEqual(InventoryAllocator.bestShipment(order, warehouses), expected)

if __name__ == '__main__':
    unittest.main()
