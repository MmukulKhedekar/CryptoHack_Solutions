from Cryptodome.Util.number import long_to_bytes, bytes_to_long
from pwn import *
import json
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(100):
    received = json_recv()
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    if received["type"] == "base64":
        encoded = base64.b64decode(received["encoded"]).decode('utf-8')
    elif received["type"] == "hex":
        encoded = bytes.fromhex(received["encoded"]).decode('utf-8')
    elif received["type"] == "rot13":
        encoded = codecs.encode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
        encoded = bytes.fromhex(received["encoded"][2:]).decode('utf-8')
    elif received["type"] == "utf-8":
        encoded = ""
        for b in received["encoded"]:
            encoded += chr(b)
    to_send = {
        "decoded": encoded
    }
    json_send(to_send)
res = r.recv()
print(res)

# crypto{3nc0d3_d3c0d3_3nc0d3}
