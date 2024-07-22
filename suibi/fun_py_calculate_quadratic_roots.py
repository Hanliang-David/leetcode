# fun_py_calculate_quadratic_roots.py
import math

def fun_py_calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        return None

print(fun_py_calculate_quadratic_roots(1, -3, 2))
