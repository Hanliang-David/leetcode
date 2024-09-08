# func_py_calculate_average.py
def func_py_calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

print(func_py_calculate_average([1, 2, 3, 4, 5]))
