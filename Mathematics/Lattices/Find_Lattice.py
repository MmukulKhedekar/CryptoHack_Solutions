from Cryptodome.Util.number import *

(q,h) = (7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257, 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800)
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

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

u = [1, h]
v = [0, q]
u,v = Lattice_Reduction(u,v)
f = u[0]
g = u[1]
a = (f*e)%q
print(long_to_bytes((a*pow(f,-1,g))%g))

## crypto{Gauss_lattice_attack!}