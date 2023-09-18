from pwn import *
from Cryptodome.Util.number import *

r = remote("socket.cryptohack.org", 13391)
print(r.recvline())
r.sendline(b'{"option": "get_signature"}')
x = eval(r.recvline().decode().strip('\n'))
N = x["N"]
e = x["e"]
s = x["signature"]
print(N,e,s)
msg = "We are hyperreality and Jack and we own CryptoHack.org"
print(b'{"option": "verify", "N": \"' + str(N).encode() + b'\", "e": \"' + str(e).encode() + b'\", "msg": \"' + str(msg).encode() + b'\"}')
r.sendline(b'{"option": "verify", "N": \"' + str(N).encode() + b'\", "e": \"' + str(e).encode() + b'\", "msg": \"' + str(msg).encode() + b'\"}')
print(r.recvline())