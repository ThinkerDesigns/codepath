#WIP
def get_items_to_restock(products, restock_threshold):
    result = []
    for x in products.keys():
        if products.get(x) < restock_threshold:
            result.append(products.get(x))
    return result
products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold))