# func_py_reverse_words.py

def func_py_reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

def test_reverse_words():
    sentences = [
        "Hello world",
        "Python is awesome",
        "I love programming",
        "Keep pushing forward",
    ]
    for sentence in sentences:
        print(f"Original: {sentence}, Reversed: {func_py_reverse_words(sentence)}")

if __name__ == "__main__":
    test_reverse_words()
