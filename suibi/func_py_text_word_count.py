# func_py_text_word_count.py
import re
from collections import Counter

def func_py_text_word_count(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

text = "Hello world! Hello Python. Python is great."
print(func_py_text_word_count(text))
