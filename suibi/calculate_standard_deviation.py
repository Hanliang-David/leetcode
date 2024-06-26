# calculate_standard_deviation.py
import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

if __name__ == "__main__":
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    stddev = calculate_standard_deviation(numbers)
    print(f"The standard deviation is {stddev}")
