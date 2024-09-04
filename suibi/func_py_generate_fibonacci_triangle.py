# func_py_generate_fibonacci_triangle.py
def func_py_generate_fibonacci_triangle(rows):
    fibs = [0, 1]
    while len(fibs) < rows * (rows + 1) // 2:
        fibs.append(fibs[-1] + fibs[-2])
    triangle = []
    index = 0
    for i in range(1, rows + 1):
        row = fibs[index:index + i]
        triangle.append(row)
        index += i
    return triangle

print(func_py_generate_fibonacci_triangle(5))
