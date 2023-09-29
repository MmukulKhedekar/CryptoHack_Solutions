import math
import random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from gmpy2 import *

primes = []

def sieve(maximum=10000):
    # In general Sieve of Sundaram, produces primes smaller
    # than (2*x + 2) for a number given number x. Since
    # we want primes smaller than maximum, we reduce maximum to half
    # This array is used to separate numbers of the form
    # i+j+2ij from others where 1 <= i <= j
    marked = [False]*(int(maximum/2)+1)

    # Main logic of Sundaram. Mark all numbers which
    # do not generate prime number by doing 2*i+1
    for i in range(1, int((math.sqrt(maximum)-1)/2)+1):
        for j in range(((i*(i+1)) << 1), (int(maximum/2)+1), (2*i+1)):
            marked[j] = True

    # Since 2 is a prime number
    primes.append(2)

    # Print other primes. Remaining primes are of the
    # form 2*i + 1 such that marked[i] is false.
    for i in range(1, int(maximum/2)):
        if (marked[i] == False):
            primes.append(2*i + 1)

def get_primorial(n):
    result = 1
    for i in range(n):
        print(primes[i])
        result = result * primes[i]
    return result

sieve()
M = get_primorial(40)
print(M)

n = 4013610727845242593703438523892210066915884608065890652809524328518978287424865087812690502446831525755541263621651398962044653615723751218715649008058509
e = 65537

print(n//(M**2))

k1 = 4313467*22
k2 = 17467*87251

