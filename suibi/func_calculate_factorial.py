# func_calculate_factorial.py
def func_calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * func_calculate_factorial(n-1)

print(func_calculate_factorial(5))
