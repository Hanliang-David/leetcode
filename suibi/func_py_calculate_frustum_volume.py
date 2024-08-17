# func_py_calculate_frustum_volume.py
import math

def func_py_calculate_frustum_volume(radius1, radius2, height):
    return (1/3) * math.pi * height * (radius1**2 + radius2**2 + radius1 * radius2)

print(func_py_calculate_frustum_volume(5, 3, 10))
