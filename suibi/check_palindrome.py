# check_palindrome.py
def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
