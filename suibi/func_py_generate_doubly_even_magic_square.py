# func_py_generate_doubly_even_magic_square.py
def func_py_generate_doubly_even_magic_square(n):
    magic_square = [[(n * i + j + 1) for j in range(n)] for i in range(n)]
    
    for i in range(0, n // 4):
        for j in range(0, n // 4):
            magic_square[i][j] = n*n + 1 - magic_square[i][j]
            
    for i in range(0, n // 4):
        for j in range(3 * n // 4, n):
            magic_square[i][j] = n*n + 1 - magic_square[i][j]
    
    for i in range(3 * n // 4, n):
        for j in range(0, n // 4):
            magic_square[i][j] = n*n + 1 - magic_square[i][j]
    
    for i in range(3 * n // 4, n):
        for j in range(3 * n // 4, n):
            magic_square[i][j] = n*n + 1 - magic_square[i][j]
    
    return magic_square

print(func_py_generate_doubly_even_magic_square(4))
