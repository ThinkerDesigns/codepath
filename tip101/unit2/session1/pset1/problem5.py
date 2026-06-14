def restock_inventory(current_inventory, restock_list):
    result = current_inventory.copy()
    for x in range(len(current_inventory)):
        if list(restock_list)[x] not in result:
            result[list(restock_list)[x]] = list(restock_list.values())[x]
        else:
            result[list(restock_list)[x]] = list(restock_list.values())[x] + result[list(restock_list)[x]]
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
print(restock_inventory(current_inventory,restock_list)) # I don't know how to print it in that JSON format the output has.