# func_py_generate_balanced_numbers.py
def func_py_generate_balanced_numbers(limit):
    def is_balanced(num):
        str_num = str(num)
        half = len(str_num) // 2
        left_sum = sum(int(digit) for digit in str_num[:half])
        right_sum = sum(int(digit) for digit in str_num[-half:])
        return left_sum == right_sum

    return [n for n in range(10, limit) if is_balanced(n)]

print(func_py_generate_balanced_numbers(1000))
