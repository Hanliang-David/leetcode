# check_armstrong_number.py
def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == n

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
