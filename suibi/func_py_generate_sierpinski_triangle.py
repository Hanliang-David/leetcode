# func_py_generate_sierpinski_triangle.py
def func_py_generate_sierpinski_triangle(n):
    triangle = ["1"]
    for _ in range(n):
        triangle = [prev + " " + prev for prev in triangle]
    return "\n".join(triangle)

print(func_py_generate_sierpinski_triangle(4))
