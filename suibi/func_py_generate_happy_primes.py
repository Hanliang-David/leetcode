# func_py_generate_happy_primes.py
def func_py_generate_happy_primes(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    def is_happy(num):
        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            num = sum(int(digit)**2 for digit in str(num))
        return num == 1
    
    return [n for n in range(1, limit) if is_prime(n) and is_happy(n)]

print(func_py_generate_happy_primes(100))
