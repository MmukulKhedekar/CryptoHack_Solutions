from sage.all import *
p = 2**(255) - 19
E = EllipticCurve(GF(p), [0, 486662, 0, 1, 0])
G = E.lift_x(9)
a = 0x1337c0decafe
print((a*G)[0])

# crypto{49231350462786016064336756977412654793383964726771892982507420921563002378152}