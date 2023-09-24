from Crypto.Util.number import *
from pwn import *
import hashlib 
import time

def generate_key():
    current_time = int(time.time())
    key = long_to_bytes(current_time)
    return hashlib.sha256(key).digest()

def encrypt(b,key):
    assert len(b) <= len(key), "Data package too large to encrypt"
    ciphertext = b''
    for i in range(len(b)):
        print(b[i], key[i], b[i]^key[i])
    for i in range(len(b)):
        ciphertext += bytes([b[i] ^ key[i]])
    return ciphertext.hex()

x = hashlib.sha256(long_to_bytes(int(time.time())+1)).digest()

r = remote('socket.cryptohack.org', 13372, level = 'DEBUG')
r.recv()

r.sendline(b'{\"option\": \"get_flag\"}')
param = eval(r.recvline().strip(b'\n').decode())
print(param["encrypted_flag"])    
enc_flag = long_to_bytes(int(param["encrypted_flag"],16))
print(long_to_bytes(int(encrypt(enc_flag,x),16)))


