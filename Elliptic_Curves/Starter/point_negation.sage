from sage.all import *
from Cryptodome.Util.number import *
## set up elliptic curve parameters
p = 9739
E = EllipticCurve(Zmod(p),[497,1768])
## perform point negation
P = E(8045,6936)
print(-P)

# crypto{8045,2803}