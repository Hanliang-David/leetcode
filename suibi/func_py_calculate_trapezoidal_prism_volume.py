# func_py_calculate_trapezoidal_prism_volume.py
def func_py_calculate_trapezoidal_prism_volume(base1, base2, height, length):
    area = ((base1 + base2) / 2) * height
    return area * length

print(func_py_calculate_trapezoidal_prism_volume(5, 7, 4, 10))
