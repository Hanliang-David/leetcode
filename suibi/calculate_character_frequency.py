# calculate_character_frequency.py
def character_frequency(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == "__main__":
    text = input("Enter a text: ")
    frequencies = character_frequency(text)
    for char, count in frequencies.items():
        print(f"{char}: {count}")
