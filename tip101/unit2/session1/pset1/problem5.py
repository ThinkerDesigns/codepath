# WIP - think im close
def restock_inventory(current_inventory, restock_list):
    result = {}
    for x in range(len(current_inventory)):
        result[list(restock_list)] = list(restock_list.values())[x] + list(current_inventory.keys())[x]
    return result
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
restock_inventory(current_inventory,restock_list)