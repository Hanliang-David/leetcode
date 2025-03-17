# func_py_find_factors.py

def func_py_find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def test_find_factors():
    numbers = [10, 15, 28, 36]
    for num in numbers:
        print(f"Factors of {num}: {func_py_find_factors(num)}")

if __name__ == "__main__":
    test_find_factors()
