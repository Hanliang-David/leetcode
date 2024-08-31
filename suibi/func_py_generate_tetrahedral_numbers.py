# func_py_generate_tetrahedral_numbers.py
def func_py_generate_tetrahedral_numbers(limit):
    tetrahedral_numbers = [(n * (n + 1) * (n + 2)) // 6 for n in range(1, limit + 1)]
    return tetrahedral_numbers

print(func_py_generate_tetrahedral_numbers(10))
