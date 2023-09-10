from sage.all import *
from Cryptodome.Util.number import *
## set up the elliptic curve parameters
p = 9739
E = EllipticCurve(Zmod(p),[497,1768])
## perform scalar multiplication
P = E(2339, 2213)
print(7863*P)

# crypto{9467,2742}