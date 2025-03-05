# func_py_find_duplicates_and_count.py
def func_py_find_duplicates_and_count(lst):
    duplicates = {}
    for item in lst:
        if lst.count(item) > 1:
            duplicates[item] = lst.count(item)
    return duplicates
