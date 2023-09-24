from Crypto.Util.number import *
from Crypto.Cipher import AES
from sage.all import *
from hashlib import *
from pwn import *
import json

r = remote('socket.cryptohack.org', 13379, level = 'DEBUG')
r.recvuntil(b'Send to Bob: ')
r.send(b'{\"supported\": [\"DH64\"]}')
r.recvuntil(b'Send to Alice: ')
r.send(b'{\"chosen\": \"DH64\"}')
data = r.recv()
param_a, param_b, param_enc, wasted = list(map(bytes, data.split(b'\n')))
print(param_a)
print(param_b)
print(param_enc)
param_a = json.loads(param_a.lstrip(b'Intercepted from Alice: ').decode())
param_b = json.loads(param_b.lstrip(b'Intercepted from Bob: ').decode())
param_enc = json.loads(param_enc.lstrip(b'Intercepted from Alice: ').decode())
p = param_a["p"]
g = param_a["g"]
A = param_a["A"]
B = param_b["B"]
iv = param_enc["iv"]
enc = param_enc["encrypted_flag"]
p = int(p,16)
g = int(g,16)
A = int(A,16)
B = int(B,16)

# print(p)
# print(g)
# print(A)
# print(B)

Zp = Integers(p)
A = Zp(A)
B = Zp(B)
g = Zp(g)
a = discrete_log(A,g,algorithm='rho')

s = pow(B,a,p)

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def pkcs7_unpad(message, block_size=16):
    if len(message) == 0:
        raise Exception("The input data must contain at least one byte")
    if not is_pkcs7_padded(message):
        return message
    padding_len = message[-1]
    return message[:-padding_len]

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return pkcs7_unpad(plaintext).decode('ascii')

print(decrypt_flag(s,iv,encrypted_flag))

# crypto{d0wn6r4d35_4r3_d4n63r0u5}
