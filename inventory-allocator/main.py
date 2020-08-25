from typing import List, Dict
import collections
class InventoryAllocator:
    @classmethod
    def cheapest_shipment(cls, items: Dict[str, int], warehouses: List[Dict]):
        """
            preconditions:
                - assume all item quantities in items & warehouses are > 0
                and <2^32 - 1
                - assume every dictionary object in warehouses have distinct
                'name' value associated with its 'name' key
        """
        if not items or not warehouses:return []
        shipment = collections.defaultdict(dict)
        for key,val in items.items():
            count = 0
            for warehouse in warehouses:
                if key in warehouse['inventory']:
                    if warehouse['inventory'][key] + count >=val:
                        shipment[warehouse['name']][key] = val-count
                        count = val
                        break
                    else:
                        shipment[warehouse['name']][key] = warehouse['inventory'][key]
                        count+=warehouse['inventory'][key]
            if count != val:
                #order for this item cannot be fufilled, remove from shipment
                for item in list(shipment):
                    if key in shipment[item]:
                        del shipment[item][key]
        # post process shipment results; remove warehouses with no orders
        ans = []
        for key,val in shipment.items():
            if not val:
                continue
            else:
                ans.append({key:val})
        return ans




