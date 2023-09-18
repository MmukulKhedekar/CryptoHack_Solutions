def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    array=[]
    for i in range(4):
        for j in range(4):
            array.append(matrix[i][j])
    return array

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))
new_matrix=matrix2bytes(matrix)
for i in new_matrix:
    print(chr(i),end="")
    
# crypto{inmatrix}