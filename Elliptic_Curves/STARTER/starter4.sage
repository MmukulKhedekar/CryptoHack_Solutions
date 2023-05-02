# here's a sagemath implementation for this challenge

sage: import hashlib
sage: p = 9739
sage: F = Zmod(p)
sage: E = EllipticCurve(F,[497,1768])
sage: P = E(815,3190)
sage: print(P)
(815 : 3190 : 1)
sage: Q = P
sage: R = P
sage: n = 1828
sage: while n>0:
....:     if n%2==1:
....:         R = R+Q
....:     Q=Q+Q
....:     n=n//2
....:
sage: print(R)
(7929 : 707 : 1)
sage: print(hashlib.sha1(str('7929').encode('utf-8')).hexdigest())
80e5212754a824d3a4aed185ace4f9cac0f908bf

# crypto{80e5212754a824d3a4aed185ace4f9cac0f908bf}