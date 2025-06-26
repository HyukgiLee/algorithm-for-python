# This program find maximum number in the list
# input : list of numbers (list)
# output : maximum number in the list (int)

def find_max(my_list):
    n = len(my_list)
    max_n = my_list[0]
    for i in range(n):
        if my_list[i] > max_n:
            max_n = my_list[i]
    return max_n

v = [17,92,18,33,58, 7, 33, 42]
print(find_max(v))