# Find the sum of all the multiples of 3 or 5 below 1000.
def divisibleBy(n, target):
    p = target // n
    return (n * (p + 1) * p) / 2

total = divisibleBy(3, 999) + divisibleBy(5, 999) - divisibleBy(15, 999)

print(total)