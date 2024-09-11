# func_py_fibonacci_sequence.py
def func_py_fibonacci_sequence(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

print(func_py_fibonacci_sequence(10))
