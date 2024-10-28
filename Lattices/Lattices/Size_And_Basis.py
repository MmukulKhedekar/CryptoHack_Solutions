v = [4,6,2,5]

def dot_product(a,b,n):
    sum = 0
    for i in range(n):
        sum+=(a[i]*b[i])
    return sum
from math import sqrt
print(sqrt(dot_product(v,v,4)))