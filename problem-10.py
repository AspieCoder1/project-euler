# Sieve of Eratosthenes
import math

def sieve(n):
    # n+1 used so zero is included in the array
    m = n+1
    numbers = [True] * m
    numbers[0] = numbers[1] = False
    for i in range(2, int(n**0.5)+1):
        if numbers[i]:
            for j in range(i*i, n+1, i):
                numbers[j] = False
    return numbers


def compute(n):
    total = 0
    primes = sieve(n)
    for i, val in enumerate(primes):
        if val:
            total += i
    return str(total)


print(compute(2000000))

# A much quicker way
import eulerlib
primes = eulerlib.primes(2000000)
total = 0
for prime in primes:
    total += prime
print(total)
