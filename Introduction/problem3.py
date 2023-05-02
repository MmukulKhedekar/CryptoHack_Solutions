from pwn import *
host, port='socket.cryptohack.org', 11112
r = remote(host,port)

res = (r.recv())
r.sendline(b'{"buy":"flag"}')
rem = (r.recvline())
print(rem)
r.close()

# b'{"flag": "crypto{sh0pp1ng_f0r_fl4g5}"}\n'
