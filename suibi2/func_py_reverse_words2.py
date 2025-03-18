# func_py_reverse_words.py

def func_py_reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def test_reverse_words():
    sentences = ["Python is fun", "Reverse this sentence"]
    for s in sentences:
        print(f"Original: {s} -> Reversed: {func_py_reverse_words(s)}")

if __name__ == "__main__":
    test_reverse_words()
