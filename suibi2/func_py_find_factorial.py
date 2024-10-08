# func_py_find_factorial.py
def func_py_find_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
