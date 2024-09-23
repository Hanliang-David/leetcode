# func_py_check_prime.py
def func_py_check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(func_py_check_prime(29))
