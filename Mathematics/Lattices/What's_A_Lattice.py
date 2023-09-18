import numpy as np
def abs(x):
    if x<0:
        return (-1)*x
    return x
v1 = [6, 2, -3]
v2 = [5, 1, 4]
v3 = [2, 7, 1]
matrix = np.array([v1,v2,v3])
print(round(abs(np.linalg.det(matrix))))

# 255
