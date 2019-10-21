from eulerlib import is_square, primes

(is_sq, sqroot) = is_square(600851475143)

p = primes(sqroot + 1)

for i in range(0, len(p) + 1):
    j = 0 - i

    if 600851475143 % p[j] == 0:
        print(p[j])
        break