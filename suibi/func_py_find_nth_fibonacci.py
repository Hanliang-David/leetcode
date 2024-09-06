# func_py_find_nth_fibonacci.py
def func_py_find_nth_fibonacci(n):
    if n <= 1:
        return n
    else:
        return func_py_find_nth_fibonacci(n-1) + func_py_find_nth_fibonacci(n-2)

print(func_py_find_nth_fibonacci(10))
