# func_py_calculate_fibonacci.py
def func_py_calculate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(func_py_calculate_fibonacci(10))
