def euc_gcd(a,b):
    if b==0:
        return a
    else:
        return euc_gcd(b,a%b)
a = 66528
b = 52920
print(euc_gcd(a,b))

# 1512