from typing import List, Dict
import collections

class InventoryAllocator:
    def _post_process_shipment(self, shipment: Dict[str,Dict[str,int]]) -> List[Dict[str,Dict[str,int]]]:
        ans = []
        for key,val in shipment.items():
            if not val:
                continue
            else:
                ans.append({key:val})
        return ans

    def cheapest_shipment(self, items: Dict[str, int], warehouses: List[Dict]) -> List[Dict[str,Dict[str,int]]]:
        """
            preconditions:
                - assume warehouses presorted based on cost
                - assume integer arguments are 32 bit signed, <=2^32 -1
                - assume integer arguments in items are > 0; invalid order if ordering <= 0 of an item
                - assume integer arguments in warehouses >= 0
                - assume every top level dictionary object in warehouses have distinct
                'name' value associated with its 'name' key
        """
        # either arguments are empty, impossible to fufill a shipment
        if not items or not warehouses:return []
        # initialize shipment container
        shipment = collections.defaultdict(dict)
        for key,val in items.items():
            count = 0
            # greedily select items from lowest cost warehouse to next
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
        return self._post_process_shipment(shipment)




