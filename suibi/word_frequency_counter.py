# word_frequency_counter.py
from collections import Counter

def word_frequency(text):
    words = text.split()
    return Counter(words)

if __name__ == "__main__":
    text = input("Enter a text: ")
    frequencies = word_frequency(text)
    for word, count in frequencies.items():
        print(f"{word}: {count}")
