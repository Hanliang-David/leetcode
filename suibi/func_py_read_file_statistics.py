# func_py_read_file_statistics.py
def func_py_read_file_statistics(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)
    return num_lines, num_words, num_chars

# 示例用法
# 请确保有一个名为 "sample.txt" 的文本文件
print(func_py_read_file_statistics("sample.txt"))
