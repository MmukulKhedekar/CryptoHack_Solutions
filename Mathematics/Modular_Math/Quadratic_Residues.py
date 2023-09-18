p = 29
ints = [14, 6, 11]
for i in ints:
    print(pow(i,(p-1)//2,p),end=" ")
qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"\nflag{ {min(qr)}}")

# flag{8}