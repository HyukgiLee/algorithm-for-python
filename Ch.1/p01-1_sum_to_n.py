# This program calculates the sum from 1 to n
# input : n (int)
# output : the sum of integers 1 to n(int)

def total_sum(n):
    return sum(i for i in range(1,n+1))

print(total_sum(10))
print(total_sum(100))