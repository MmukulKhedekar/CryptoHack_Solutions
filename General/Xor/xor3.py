from Cryptodome.Util.number import *
from pwn import xor 

s = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
s = bytes.fromhex(s)
for i in range(256):
    ans = xor(s,i)
    if b'crypto' in ans:
        print(ans)

# crypto{0x10_15_my_f4v0ur173_by7e}