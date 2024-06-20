# string_hash.py
import hashlib

def get_string_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

string = "Hello, World!"
hash_value = get_string_hash(string)
print(f"String: {string}")
print(f"SHA-256 Hash: {hash_value}")
