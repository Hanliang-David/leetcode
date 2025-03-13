# func_py_anagram_checker.py
from collections import Counter

def func_py_anagram_checker(str1, str2):
    return Counter(str1.replace(" ", "").lower()) == Counter(str2.replace(" ", "").lower())

print(func_py_anagram_checker("listen", "silent"))
print(func_py_anagram_checker("hello", "world"))
