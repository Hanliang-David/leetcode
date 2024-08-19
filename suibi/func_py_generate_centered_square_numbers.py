# func_py_generate_centered_square_numbers.py
def func_py_generate_centered_square_numbers(n):
    return [i**2 + (i - 1)**2 for i in range(1, n + 1)]

print(func_py_generate_centered_square_numbers(10))
