# func_py_find_median.py
def func_py_find_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

print(func_py_find_median([10, 20, 30, 40, 50]))
