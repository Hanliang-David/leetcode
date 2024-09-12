# func_py_find_factorial.py
def func_py_find_factorial(n):
    if n == 0:
        return 1
    return n * func_py_find_factorial(n-1)

print(func_py_find_factorial(5))
