v = [2,6,3]
w = [1,0,0]
u = [7,7,2]

def dot_product(a,b,n):
    sum = 0
    for i in range(n):
        sum+=(a[i]*b[i])
    return sum
def scalar_multiplication(k,a,n):
    for i in range(n):
        a[i]=k*a[i]
    return a 
def subtraction(a,b,n):
    list2 = []
    for i in range(n):
        list2.append(a[i]-b[i])
    return list2

# 3*(2*v-w) \cdot 2*u

print(dot_product(scalar_multiplication(3,subtraction(scalar_multiplication(2,v,3),w,3),3),scalar_multiplication(2,u,3),3))

# 702