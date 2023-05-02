# here's a sagemath implementation

sage: p = 9739
sage: F = Zmod(p)
sage: E = EllipticCurve(F,[497,1768])
sage: P = E(2339,2213)
sage: print(P)
(2339 : 2213 : 1)
sage: Q = P
sage: R = P
sage: n = 7862
sage: while n>0:
....:     if n%2==1:
....:         R = R+Q
....:     Q=Q+Q
....:     n=n//2
....:
sage: print(R)
(9467 : 2742 : 1)

# crypto{9467,2742}