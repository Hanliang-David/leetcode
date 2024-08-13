# func_py_calculate_pentagon_area.py
import math

def func_py_calculate_pentagon_area(side_length):
    return (5 * side_length**2) / (4 * math.tan(math.pi / 5))

print(func_py_calculate_pentagon_area(6))
