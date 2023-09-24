from Crypto.Util.number import *
from Crypto.Cipher import AES
from pwn import remote
import hashlib
import json

r = remote('socket.cryptohack.org', 13373, level = 'DEBUG')
param_a = json.loads(r.recvline().lstrip(b'Intercepted from Alice: ').rstrip(b'\n').decode())
p = param_a["p"]
g = param_a["g"]
A = param_a["A"]
param_b = json.loads(r.recvline().lstrip(b'Intercepted from Bob: ').rstrip(b'\n').decode())
B = param_b["B"]
param_enc = json.loads(r.recvline().lstrip(b'Intercepted from Alice: ').rstrip(b'\n').decode())
iv = param_enc["iv"]
enc = param_enc["encrypted"]
print(p)
print(A)
print(B)
print(iv)
print(enc)
print(r.recvuntil(b'Bob connects to you, send him some parameters: '))
r.sendline(b'{\"p\": \"' + p.encode() + b'\", \"g\": \"' + g.encode() + b'\", \"A\": \"' + p.encode() + b'\"}')
print(r.recvline())

param_enc = json.loads(r.recvline().lstrip(b'Bob says to you: ').rstrip(b'\n').decode())
iv = param_enc["iv"]
enc = param_enc["encrypted"]
print(iv)
print(enc)

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

print(decrypt_flag(0,iv,enc))