import eulerlib

arr = eulerlib.primes(2000000)

total = 0
for i in arr:
    total += i

print(total)