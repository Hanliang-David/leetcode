# simple_regex_match.py
import re

def regex_match(pattern, text):
    matches = re.findall(pattern, text)
    return matches

if __name__ == "__main__":
    pattern = input("Enter regex pattern: ")
    text = input("Enter text: ")
    matches = regex_match(pattern, text)
    if matches:
        print(f"Matches found: {matches}")
    else:
        print("No matches found")
