# func_py_generate_acronym.py
def func_py_generate_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

print(func_py_generate_acronym("random access memory"))
