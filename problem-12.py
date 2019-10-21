import itertools, math

def factor(n):
    # we need to only consider the factors up to root n as we would then get duplicates
	end = int(math.sqrt(n))
	result = sum(2
		for i in range(1, end + 1)
		if n % i == 0)
	if end**2 == n:
		result -= 1
	return result

def compute():
    n=0
    # counts up in ones in an efficient way
    for i in itertools.count(1):
        n +=i 
        if factor(n) > 500:
            return str(n)

print(compute())


