# WIP
def merge_catalogs(catalog1, catalog2):
    result = catalog1
    for x in result:
        if x in catalog2:
            result[catalog2[x]] = max(catalog1[x],catalog2[x])
    return result
catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1,catalog2))