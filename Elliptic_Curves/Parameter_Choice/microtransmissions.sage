from Crypto.Util.number import *
from Crypto.Random import random
from Crypto.Cipher import AES
from Crypto.Util.number import inverse
from Crypto.Util.Padding import pad, unpad
from sage.all import *
from sage.groups.generic import bsgs
import hashlib

# curve parameters 
a = 1
b = 4
p = 99061670249353652702595159229088680425828208953931838069069584252923270946291
E = EllipticCurve(GF(p),[a,b])

G = E(43190960452218023575787899214023014938926631792651638044680168600989609069200, 20971936269255296908588589778128791635639992476076894152303569022736123671173)

ax = 87360200456784002948566700858113190957688355783112995047798140117594305287669
bx = 6082896373499126624029343293750138460137531774473450341235217699497602895121
A = E.lift_x(ax)
B = E.lift_x(bx)

# print(E.order())
# print(G.order())
# print(A.order())

assert E.order() == G.order() and E.order() == A.order()

def dlp_solve(G,A):
    primes = []
    for i in G.order().factor():
        if (len(primes)<8):
            primes.append(i)
        else:
            break
    corresponding_dlp = [0]*len(primes)
    for i,(p_i,e_i) in enumerate(primes):
        for j in range(e_i):
            corresponding_dlp[i]+=bsgs(G*(G.order()//p_i),(A-(G*corresponding_dlp[i]))*(G.order()//(p_i**(j+1))),(0,p_i),operation='+')*(p_i**j)
    return crt(corresponding_dlp,[p_i**e_i for (p_i,e_i) in primes])

n_a = dlp_solve(G,A)

def gen_shared_secret(P, n):
	S = n*P
	return S.xy()[0]

share_secret = gen_shared_secret(B,n_a)

def decrypt(shared_secret,encrypted_flag,iv):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    cipher = AES.new(key,AES.MODE_CBC,iv)
    return cipher.decrypt(encrypted_flag)

share_secret = 92209717447332837440641806732517921920015580446111641942522142444036785043977
iv = "ceb34a8c174d77136455971f08641cc5"
encrypted_flag = "b503bf04df71cfbd3f464aec2083e9b79c825803a4d4a43697889ad29eb75453"
print(decrypt(share_secret,bytes.fromhex(encrypted_flag),bytes.fromhex(iv)))

## crypto{d0nt_l3t_n_b3_t00_sm4ll}