from sage.all import *
from Cryptodome.Util.number import *
from hashlib import sha1
## setup elliptic curve parameters
E = EllipticCurve(GF(9739),[497,1768])
QA = E(815, 3190)
nB = 1829
print(sha1(str((nB*QA)[0]).encode()).hexdigest()) 
# crypto{80e5212754a824d3a4aed185ace4f9cac0f908bf}