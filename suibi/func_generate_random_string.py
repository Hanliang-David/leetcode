# func_generate_random_string.py
import random
import string

def func_generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

print(func_generate_random_string(10))
