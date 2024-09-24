# func_py_sum_odd_numbers.py
def func_py_sum_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0)

print(func_py_sum_odd_numbers([1, 2, 3, 4, 5]))
