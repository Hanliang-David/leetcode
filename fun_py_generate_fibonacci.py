# fun_py_generate_fibonacci.py

def fun_py_generate_fibonacci(n):
    fib_series = [0, 1]
    for _ in range(n - 2):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

def test_generate_fibonacci():
    n = 10
    print(f"Fibonacci series of {n}: {fun_py_generate_fibonacci(n)}")

if __name__ == "__main__":
    test_generate_fibonacci()
