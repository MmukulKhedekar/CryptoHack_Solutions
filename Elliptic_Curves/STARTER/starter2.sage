from sage.all import *
from Cryptodome.Util.number import *
## set up elliptic curve parameters
p = 9739
E = EllipticCurve(Zmod(p),[497,1768])
## define the points and perform point addition
P = E(493, 5564)
Q = E(1539, 4742)
R1 = E(4403,5202)

print(P+P+Q+R1)
# crypto{4215,2162}