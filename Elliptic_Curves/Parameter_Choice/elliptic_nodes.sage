from sage.all import *
from Crypto.Util. number import *

## Two points on the Elliptic Curve can leak the parameters 
p = 4368590184733545720227961182704359358435747188309319510520316493183539079703

gx = 8742397231329873984594235438374590234800923467289367269837473862487362482
gy = 225987949353410341392975247044711665782695329311463646299187580326445253608
qx = 2582928974243465355371953056699793745022552378548418288211138499777818633265
qy = 2421683573446497972507172385881793260176370025964652384676141384239699096612

a = ((pow(gy,2,p) - pow(qy,2,p) - pow(gx,3,p) + pow(qx,3,p))*(pow(gx-qx,-1,p)))%p 
b = (pow(gy,2,p) - pow(gx,3,p) - a*gx)%p
c = (pow(qy,2,p) - pow(qx,3,p) - a*qx)%p
assert pow(gy,2,p) == (pow(gx,3,p) + a*gx + b)%p
assert pow(qy,2,p) == (pow(qx,3,p) + a*qx + b)%p

## Realise that the elliptic curve is singular
# E = EllipticCurve(GF(p),[a,b])

## Check if that's true using 4A^3 + 27B^2 = 0
# print((4*a**3+27*b**2)%p)
# P.<x> = PolynomialRing(GF(p),x)
# f = x**3 + a*x + b
# print(f.roots())

## Discrete Logarithm Problem for Singular Curves

P.<x> = PolynomialRing(GF(p),x)
f = x**3 + a*x + b
P = (gx, gy)
Q = (qx, qy)
## to calculate the affine shifts, execute print(f.factors())
f_ = f.subs(x=x + 1557923326969252180825193218688702224840389936248863823173183835359957757721)
P_ = (P[0] - 1557923326969252180825193218688702224840389936248863823173183835359957757721, P[1])
Q_ = (Q[0] - 1557923326969252180825193218688702224840389936248863823173183835359957757721, Q[1])
d = 1557923326969252180825193218688702224840389936248863823173183835359957757721 - 1252743530795041358577574745326954908754967315811591864173948822463623564261
t = GF(p)(d).square_root()

u = (P_[1] + t*P_[0])/(P_[1] - t*P_[0]) % p
v = (Q_[1] + t*Q_[0])/(Q_[1] - t*Q_[0]) % p
print(long_to_bytes(discrete_log(v, u)))

## crypto{s1ngul4r_s1mplif1c4t1on}