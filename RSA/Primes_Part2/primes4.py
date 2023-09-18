from Cryptodome.Util.number import *
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

s = "D:\ctfs\crypto\CryptoHack_Solutions\RSA\Primes_Part2\\"
pub_key = []
pub_exp = []
for i in range(1,51):
    f = open(s+str(i)+".pem","rb").read()
    key = RSA.import_key(f)
    pub_key.append(key.n)
    pub_exp.append(key.e)
from math import gcd
for i in range(len(pub_key)):
    for j in range(i+1,len(pub_key)):
        if gcd(pub_key[i],pub_key[j])>1:
            n = pub_key[i]
            p = gcd(pub_key[i], pub_key[j])
            q = n//p
            phi = (p-1)*(q-1)
            c = int(open(f"{s}{i+1}.ciphertext","rb").read().decode(),16)           
            d = pow(pub_exp[i],-1,phi)
            key = RSA.construct((n,pub_exp[i],d))
            cipher = PKCS1_OAEP.new(key)
            print(cipher.decrypt(long_to_bytes(c)))
            
# crypto{3ucl1d_w0uld_b3_pr0ud}
