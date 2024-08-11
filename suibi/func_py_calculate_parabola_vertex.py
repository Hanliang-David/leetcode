# func_py_calculate_parabola_vertex.py
def func_py_calculate_parabola_vertex(a, b, c):
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    return (h, k)

print(func_py_calculate_parabola_vertex(1, -2, 1))
