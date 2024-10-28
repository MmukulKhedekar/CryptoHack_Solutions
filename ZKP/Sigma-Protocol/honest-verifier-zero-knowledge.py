from pwn import *
from Crypto.Util.number import *
import random 
import json 

host = 'socket.cryptohack.org'
port = 13427
r = remote(host, port, level='DEBUG')

p = 0x1ed344181da88cae8dc37a08feae447ba3da7f788d271953299e5f093df7aaca987c9f653ed7e43bad576cc5d22290f61f32680736be4144642f8bea6f5bf55ef
q = 0xf69a20c0ed4465746e1bd047f57223dd1ed3fbc46938ca994cf2f849efbd5654c3e4fb29f6bf21dd6abb662e911487b0f9934039b5f20a23217c5f537adfaaf7
g = 2

r.recvuntil(b'Send me a transcript for my given `e` proving that you know the flag `w` such that y = g^w mod p\n')

response = json.loads(r.recvline().strip().decode())
e = response["e"]
y = response["y"]

a = pow(pow(y, e, p), -1, p)
z = 0

challenge = {
    "a": a,
    "z": z
}
payload = json.dumps(challenge).encode()

r.sendline(payload)
r.interactive()

## crypto{so_honest_very_zero_knowledge}