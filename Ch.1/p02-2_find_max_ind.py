# This program finds the index of the max number from the given list.
# input : list of integers (list)
# output : index of the max number (int)

def find_max_ind_v1(my_list):
    n = len(my_list)
    max_num = my_list[0]
    for i in range(n):
        if my_list[i] > max_num:
            max_num = my_list[i]
    return my_list.index(max_num)
    
# v2 function uses extra variable inside to get index without using .index
# input : list of integers (list)
# output : index of the max number (int)
def find_max_ind_v2(my_list):
    n = len(my_list)
    max_num = my_list[0]
    max_num_ind = 0
    for i in range(n):
        if my_list[i] > max_num:
            max_num = my_list[i]
            max_num_ind = i
    return my_list.index(max_num)
    
v = [17,92,18,33,58, 7, 33, 42]
print(find_max_ind_v1(v))
print()
print(find_max_ind_v2(v))