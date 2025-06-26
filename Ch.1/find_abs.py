# import library
import math

# find sign of absolute variable
# input : integer number(int)
# output : absolute value of number(int)

def abs_sign(num):
    if num >= 0:
        return num
    else:
        return -num
    
# find absolute value using math function(math.sqrt)
# input : integer number(int)
# output : absolute value of the input(int)

def abs_square(num):
    num_sq = num* num
    return int(math.sqrt(num_sq))

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(7))
print(abs_square(-4))