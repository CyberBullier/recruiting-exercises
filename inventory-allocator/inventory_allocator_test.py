import unittest

from main import InventoryAllocator

class InventoryAllocatorTest(unittest.TestCase):
    def test_empty_arguments(self):
        items,warehouses = {},[{'name':'w1','inventory':{'apple':3}}]
        self.assertEqual([],InventoryAllocator.cheapest_shipment(items,warehouses))
        items,warehouses = {'babycow':4},[]
        self.assertEqual([],InventoryAllocator.cheapest_shipment(items,warehouses))
        items,warehouses = {},[]
        self.assertEqual([],InventoryAllocator.cheapest_shipment(items,warehouses))

    def test_no_item_in_any_warehouse(self):
        warehouses, items = [{'name':'w1','inventory':{'apple':3}}], {'babycow':3}
        self.assertEqual([],InventoryAllocator.cheapest_shipment(items,warehouses))

    def test_item_in_warehouse_not_enough(self):
        warehouses = [{'name':'w1','inventory':{'apple':3}}, {'name':'w2','inventory':{'babycow':3}}]
        items = {'babycow':5}
        self.assertEqual([],InventoryAllocator.cheapest_shipment(items,warehouses))

    def test_order_cheapest_shipment_single_warehouse(self):
        warehouses = [{'name':'w1','inventory':{'babycow':5}}, {'name':'w2','inventory':{'babycow':3}}]
        items = {'babycow':4}
        self.assertEqual([{'w1':{'babycow': 4}}],InventoryAllocator.cheapest_shipment(items,warehouses))

    def test_order_cheapest_shipment_many_warehouse(self):
        warehouses = [{'name':'w1','inventory':{'babycow':5}}, {'name':'w2','inventory':{'babycow':3}}]
        items = {'babycow':6}
        self.assertEqual([{'w1':{'babycow': 5}},{'w2':{'babycow': 1}}],InventoryAllocator.cheapest_shipment(items,warehouses))







if __name__ == "__main__":
    unittest.main()
