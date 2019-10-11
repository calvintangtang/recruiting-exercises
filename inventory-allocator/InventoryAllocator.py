'''
INPUTS
order: Dictionary (i.e. { "apple": 5, "banana": 5, "orange": 5 })
warehouses: List (i.e. [ { "name": "owd", "inventory": { "apple": 5, "orange": 10 } }, { "name": "dm":, "inventory": { 'banana': 5, "orange": 10 } } ])

OUTPUT
List of warehouse Dictionaries and items
'''
def bestShipment(order, warehouses):
    if not all(val >= 0 for val in order.values()):
        return []
    result = []

    for warehouse in warehouses:
        if not all(val >= 0 for val in warehouse["inventory"].values()):
            return []
        warehouse_name = warehouse["name"]
        w_dict = {warehouse_name: {}}

        for item in order:
            if order[item] == 0:
                continue
            if item in warehouse["inventory"].keys():
                diff = order[item] - warehouse["inventory"][item]
                if diff >= 0:
                    order[item] = diff
                    w_dict[warehouse_name][item] = warehouse["inventory"][item]
                    warehouse["inventory"][item] = 0
                else:
                    w_dict[warehouse_name][item] = order[item]
                    warehouse["inventory"][item] = warehouse["inventory"][item] - order[item]
                    order[item] = 0
        if w_dict[warehouse_name]:
            result.append(w_dict)

    if all(val != 0 for val in order.values()):
        return []
    return result
