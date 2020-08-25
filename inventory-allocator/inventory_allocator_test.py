import unittest

from main import InventoryAllocator

class InventoryAllocatorTest(unittest.TestCase):
    def test_empty_arguments(self):
        """
        tests and/or arguments are empty
        """
        items, warehouses = {}, [{"name": "w1", "inventory": {"apple": 3}}]
        expected = []
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )
        items, warehouses = {"babycow": 4}, []
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )
        items, warehouses = {}, []
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )

    def test_no_item_in_warehouse(self):
        """
        tests when an order item isn't present in any warehouse
        """
        warehouses, items = [{"name": "w1", "inventory": {"apple": 3}}], {"babycow": 3}
        expected = []
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )

    def test_item_in_warehouse_not_enough(self):
        """
        tests when order item is present in warehouse but insufficient inventory

        """
        warehouses = [
            {"name": "w1", "inventory": {"apple": 3}},
            {"name": "w2", "inventory": {"babycow": 3}},
        ]
        items = {"babycow": 5}
        expected = []
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )

    def test_item_in_many_warehouse_not_enough_and_enough(self):
        """
        tests order items that have sufficient and insufficient inventory 
        across many warehouses
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5, "catherine": 4}},
            {"name": "w2", "inventory": {"babycow": 3, "catherine": 1}},
        ]
        items = {"babycow": 6, "catherine": 8}
        expected = [{"w1": {"babycow": 5}}, {"w2": {"babycow": 1}}]
        self.assertEqual(
            sorted(expected, key=lambda x: x.keys()),
            sorted(
                InventoryAllocator().cheapest_shipment(items, warehouses),
                key=lambda x: x.keys(),
            ),
        )

    def test_no_item_in_many_warehouse_and_not_enough(self):
        """
        tests when order items are either non existent and/or not enough
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5, "catherine": 4}},
            {"name": "w2", "inventory": {"babycow": 3, "catherine": 1}},
        ]
        items = {"babycow": 9, "katherine": 8}
        expected = []
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )

    def test_zero_item_count(self):
        """
        test when at least one warehouse has an item count of 0
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 0, "catherine": 4}},
            {"name": "w2", "inventory": {"babycow": 0, "catherine": 1}},
        ]
        items = {"babycow": 9}
        expected = []
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )

    def test_no_empty_warehouse_in_reponse(self):
        """
        tests when warehouse only has target item but item inventory is insufficient across all warehouses
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5, "catherine": 4}},
            {"name": "w2", "inventory": {"babycow": 3, "catherine": 1}},
        ]
        items = {"babycow": 5, "catherine": 8}
        expected = [{"w1": {"babycow": 5}}]
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )

    def test_order_cheapest_shipment_single_warehouse(self):
        """
        test cheapest shipment holds true
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5}},
            {"name": "w2", "inventory": {"babycow": 3}},
        ]
        items = {"babycow": 4}
        expected = [{"w1": {"babycow": 4}}]
        self.assertEqual(
            expected, InventoryAllocator().cheapest_shipment(items, warehouses)
        )

    def test_order_cheapest_shipment_many_warehouse(self):
        """
        test cheapest shipment holds true split across many warehouses
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5}},
            {"name": "w2", "inventory": {"babycow": 3}},
        ]
        items = {"babycow": 6}
        expected = [{"w1": {"babycow": 5}}, {"w2": {"babycow": 1}}]
        self.assertEqual(
            sorted(expected, key=lambda x: x.keys()),
            sorted(
                InventoryAllocator().cheapest_shipment(items, warehouses),
                key=lambda x: x.keys(),
            ),
        )


if __name__ == "__main__":
    unittest.main()
