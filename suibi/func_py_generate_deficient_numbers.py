# func_py_generate_deficient_numbers.py
def func_py_generate_deficient_numbers(limit):
    def sum_of_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)
    
    return [n for n in range(1, limit) if sum_of_divisors(n) < n]

print(func_py_generate_deficient_numbers(100))
