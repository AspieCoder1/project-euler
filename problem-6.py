def compute(n):
    sum_of_squares = 0

    for i in range(0,n+1):
        sum_of_squares += i**2

    square_of_sum = ((n*(n+1))/2)**2

    return square_of_sum - sum_of_squares

print(compute(100))