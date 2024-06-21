# read_write_json.py
import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

file_path = 'data.json'
data_to_write = {"name": "Alice", "age": 30, "city": "Wonderland"}

write_json(file_path, data_to_write)
data_read = read_json(file_path)
print(f"Data written to {file_path}: {data_to_write}")
print(f"Data read from {file_path}: {data_read}")
