# calculate_median.py
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    return median

if __name__ == "__main__":
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    median = calculate_median(numbers)
    print(f"The median is {median}")
