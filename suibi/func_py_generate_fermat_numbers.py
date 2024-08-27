# func_py_generate_fermat_numbers.py
def func_py_generate_fermat_numbers(limit):
    return [(2**(2**n) + 1) for n in range(limit)]

print(func_py_generate_fermat_numbers(5))
