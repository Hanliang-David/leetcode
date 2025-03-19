# func_py_reverse_words.py

def func_py_reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def test_reverse_words():
    text = "Python is amazing"
    print(f"Reversed words: {func_py_reverse_words(text)}")

if __name__ == "__main__":
    test_reverse_words()
