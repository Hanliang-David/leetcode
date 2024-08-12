# func_py_generate_hexagonal_numbers.py
def func_py_generate_hexagonal_numbers(n):
    return [i * (2 * i - 1) for i in range(1, n + 1)]

print(func_py_generate_hexagonal_numbers(10))
