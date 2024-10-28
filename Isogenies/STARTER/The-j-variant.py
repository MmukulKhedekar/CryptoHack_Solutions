from sage.all import *

E = EllipticCurve(GF(163), [145, 49])
print(E.j_invariant())

## 127