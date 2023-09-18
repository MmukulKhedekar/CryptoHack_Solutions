def binexp(x, y, z):
    if (y==0):
        return 1%z
    ans = binexp(x, y//2, z)
    ans = ((ans%z)*(ans%z))%z
    if (y%2):
        ans = (ans*x)%z 
    return ans 
p = 991
g = 209
print(binexp(g,p-2,p))

# 569
