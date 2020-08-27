from typing import List, Dict
import collections


def cheapest_shipment(all_orders: Dict[str, int], warehouses: List[Dict]) -> List[Dict[str,Dict[str,int]]]:
    """
        preconditions:
            - assume warehouses presorted based on cost
            - assume integer arguments are 32 bit signed, <=2^32 -1
            - assume integer arguments in items are > 0; invalid order if ordering <= 0 of an item
            - assume integer arguments in warehouses >= 0
            - assume every top level dictionary object in warehouses have distinct
            'name' value associated with its 'name' key
            -assume valid schema for input
    """
    # either arguments are empty, impossible to fufill a shipment
    if not all_orders or not warehouses:return []
    # initialize global shipment container
    shipment = collections.defaultdict(dict)
    for key,val in all_orders.items():
        count = 0
        # initialize shipment container for warehouse & invetory for order item key
        item_warehouse_shipments = collections.defaultdict(dict)
        # greedily select items from lowest cost warehouse to next
        for warehouse in warehouses:
            if key in warehouse['inventory'] and warehouse['inventory'][key]>0:
                if warehouse['inventory'][key] + count >=val:
                    item_warehouse_shipments[warehouse['name']][key] = val-count
                    count = val
                    break
                else:
                    item_warehouse_shipments[warehouse['name']][key] = warehouse['inventory'][key]
                    count+=warehouse['inventory'][key]
        #update global shipments if current order has sufficient inventory
        if val == count:
            for name,warehouse_order in item_warehouse_shipments.items():
                shipment[name].update(warehouse_order)

    return [{key:val} for key,val in shipment.items()]




