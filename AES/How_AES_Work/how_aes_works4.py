def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    array=[]
    for i in range(4):
        for j in range(4):
            array.append(matrix[i][j])
    return array

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    list2 = []
    for i in range(4):
        list3 = []
        for j in range(4):
            list3.append(s[i][j]^k[i][j])
        list2.append(list3)
    return list2

a = matrix2bytes(add_round_key(state, round_key))
for c in a:
    print(chr(c),end="")

# crypto{r0undk3y}

