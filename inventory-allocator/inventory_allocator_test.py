import unittest

from main import cheapest_shipment

class InventoryAllocatorTest(unittest.TestCase):
    def test_empty_arguments(self):
        """
        tests for empty arguments
        """
        all_orders, warehouses = {}, [{"name": "w1", "inventory": {"apple": 3}}]
        expected = []
        # assert when empty all_orders
        self.assertEqual(
            expected, cheapest_shipment(all_orders, warehouses)
        )
        all_orders, warehouses = {"babycow": 4}, []
        # assert when no warehouses
        self.assertEqual(
            expected, cheapest_shipment(all_orders, warehouses)
        )
        all_orders, warehouses = {}, []
        # assert when no orders and warehouses
        self.assertEqual(
            expected, cheapest_shipment(all_orders, warehouses)
        )

    def test_no_item_in_warehouse(self):
        """
        tests when an order item isn't present in any warehouse
        """
        warehouses, all_orders = [{"name": "w1", "inventory": {"apple": 3}}], {"babycow": 3}
        expected = []
        self.assertEqual(
            expected, cheapest_shipment(all_orders, warehouses)
        )

    def test_zero_item_count(self):
        """
        test when at least one warehouse has an item count of 0
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 0, "catherine": 4}},
        ]
        all_orders = {"babycow": 9}
        expected = []
        self.assertEqual(
            expected, cheapest_shipment(all_orders, warehouses)
        )
    def test_item_in_warehouse_not_enough(self):
        """
        tests when order item is present in warehouse, its count
        is greater than 0 but insufficient inventory

        """
        warehouses = [
            {"name": "w1", "inventory": {"apple": 3}},
            {"name": "w2", "inventory": {"babycow": 3}},
        ]
        all_orders = {"babycow": 5}
        expected = []
        self.assertEqual(
            expected, cheapest_shipment(all_orders, warehouses)
        )

    def test_item_in_many_warehouse_not_enough_and_enough(self):
        """
        tests all_orders items that have sufficient and insufficient inventory
        across many warehouses
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5, "catherine": 4}},
            {"name": "w2", "inventory": {"babycow": 3, "catherine": 1}},
        ]
        all_orders = {"babycow": 6, "catherine": 8}
        expected = [{"w1": {"babycow": 5}}, {"w2": {"babycow": 1}}]
        self.assertEqual(
            sorted(expected, key=lambda x: x.keys()),
            sorted(
                cheapest_shipment(all_orders, warehouses),
                key=lambda x: x.keys(),
            ),
        )

    def test_no_item_in_many_warehouse_and_not_enough(self):
        """
        tests when all_orders items are either non existent(order item name
        not in warehouse) and/or insufficient inventory
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5, "catherine": 4}},
            {"name": "w2", "inventory": {"babycow": 3, "catherine": 1}},
        ]
        all_orders = {"babycow": 9, "katherine": 8}
        expected = []
        self.assertEqual(
            expected, cheapest_shipment(all_orders, warehouses)
        )


    def test_order_cheapest_shipment_single_warehouse(self):
        """
        test correct cheapest shipment warehouse is selected
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5}},
            {"name": "w2", "inventory": {"babycow": 3}},
        ]
        all_orders = {"babycow": 4}
        expected = [{"w1": {"babycow": 4}}]
        self.assertEqual(
            expected, cheapest_shipment(all_orders, warehouses)
        )

    def test_order_cheapest_shipment_many_warehouse(self):
        """
        test optimality of warehouse(s) selected and their split
        """
        warehouses = [
            {"name": "w1", "inventory": {"babycow": 5}},
            {"name": "w2", "inventory": {"babycow": 3}},
        ]
        all_orders = {"babycow": 6}
        expected = [{"w1": {"babycow": 5}}, {"w2": {"babycow": 1}}]
        self.assertEqual(
            sorted(expected, key=lambda x: x.keys()),
            sorted(
                cheapest_shipment(all_orders, warehouses),
                key=lambda x: x.keys(),
            ),
        )


if __name__ == "__main__":
    unittest.main()
