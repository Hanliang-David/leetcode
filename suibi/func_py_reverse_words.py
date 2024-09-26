# func_py_reverse_words.py
def func_py_reverse_words(s):
    return ' '.join(s.split()[::-1])

print(func_py_reverse_words("hello world this is python"))
