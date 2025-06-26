# This program calculates the sum from 1 to n, using equation
# input : target integer n (int)
# output : sum from 1 to n (int)

def total_sum(n):
    return n*(n+1)//2

print(total_sum(10))
print(total_sum(100))