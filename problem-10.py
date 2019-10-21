# Sieve of Eratosthenes
def sieve(n):
    primes = []
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i**2, n+1, i):
                multiples.append(j)
    return primes

def compute(n):
    total = 0
    primes = sieve(n)
    print(primes)
    for i in primes:
        total +=i
    return str(total)

# print(compute(2000000))

# A much quicker way
import eulerlib
primes = eulerlib.primes(2000000)
total = 0
for prime in primes:
    total += prime
print(total)