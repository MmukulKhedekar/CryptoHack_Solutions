def dot_product(a,b,n):
    sum = 0
    for i in range(n):
        sum+=(a[i]*b[i])
    return sum

def Lattice_Reduction(u,v):
    if dot_product(v,v,len(v))<dot_product(u,u,len(u)):
            t = u 
            u = v 
            v = t
    m = dot_product(u,v,len(u))//dot_product(u,u,len(u))
    while m!=0: 
        if dot_product(v,v,len(v))<dot_product(u,u,len(u)):
            t = u 
            u = v 
            v = t
        m = dot_product(u,v,len(u))//dot_product(u,u,len(u))
        if (m==0):
            break
        for i in range(len(v)):
            v[i] = v[i] - m*u[i]
    return u,v

u = [87502093, 123094980]
v = [846835985, 9834798552]
x,y = Lattice_Reduction(u,v)
print(dot_product(x,y,len(x)))

## 7410790865146821
