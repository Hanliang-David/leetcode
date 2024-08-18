# func_py_generate_symmetric_numbers.py
def func_py_generate_symmetric_numbers(n):
    return [int(str(i) + str(i)[::-1]) for i in range(1, n + 1)]

print(func_py_generate_symmetric_numbers(10))
