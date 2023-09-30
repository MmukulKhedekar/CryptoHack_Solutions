from pwn import *
from Crypto.Util.number import *
from Crypto.Hash import SHA256
from utils import *
from pkcs1 import emsa_pkcs1_v15

r = remote("socket.cryptohack.org", 13391)

print(r.recvline())

r.sendline(b'{"option": "get_signature"}')
x = eval(r.recvline().decode().strip('\n'))
N = x["N"]
e = x["e"]
s = x["signature"]

print(N,e,s)
msg = r'^I am Mallory.*own CryptoHack.org$'

# print(b'{"option": "verify", "N": \"' + str(N).encode() + b'\", "e": \"' + str(e).encode() + b'\", "msg": \"' + str(msg).encode() + b'\"}')
# r.sendline(b'{"option": "verify", "N": \"' + str(N).encode() + b'\", "e": \"' + str(e).encode() + b'\", "msg": \"' + str(msg).encode() + b'\"}')
# print(r.recvline())

# MSG = 'We are hyperreality and Jack and we own CryptoHack.org'
# DIGEST = emsa_pkcs1_v15.encode(MSG.encode(), 256)
# SIGNATURE = pow(bytes_to_long(DIGEST), D, N)

digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
print(bytes_to_long(digest))