from Cryptodome.Util.number import *
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad 
import requests
import string
from pwn import xor 
import time
url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"
def encrypt(plaintext):
    url_new = url + str(plaintext) + "/"
    encrypted = eval(requests.get(url_new).text)["ciphertext"]
    return encrypted
def length_of_flag():
    length = (len(encrypt("01"))//32)*16
    i = len(encrypt("01"))
    j=1
    while len(encrypt("01"*j))==i:
        j+=1
    length -= (j-1)
    return length
flag = ''
total = 32 - 1
alphabet = '{'+'_'+'@'+'}'+string.digits+string.ascii_lowercase+string.ascii_uppercase
while True:
    payload = '1' * (total-len(flag))
    expected = encrypt(payload.encode().hex())
    for c in alphabet: 
        res = encrypt(bytes.hex((payload + flag + c).encode()))
        if res[32:64] == expected[32:64]:
            flag += c
            print(flag)
            break
    if flag.endswith('}'): break
print(flag)




