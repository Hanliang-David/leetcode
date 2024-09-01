# func_py_generate_amicable_numbers.py
def func_py_generate_amicable_numbers(limit):
    def sum_of_divisors(n):
        return sum([i for i in range(1, n) if n % i == 0])

    amicable_pairs = []
    for a in range(2, limit):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_pairs.append((a, b))

    return amicable_pairs

print(func_py_generate_amicable_numbers(3000))
