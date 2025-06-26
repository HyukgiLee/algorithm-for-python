# Create program that finds out lowest number in the list

# This program finds the lowest number from given list
# input : list of numbers(list)
# output : the lowest value number (int)

def find_min(my_list):
    n = len(my_list)
    lowest_val = my_list[0]
    for i in range(n):
        if my_list[i] < lowest_val:
            lowest_val = my_list[i]
    return lowest_val

# This program finds the index of lowest number from given list
# input : list of numbers(list)
# output : index of the lowest value number (int)

def find_min_ind(my_list):
    n = len(my_list)
    lowest_ind = 0
    for i in range(n):
        if my_list[i] < my_list[lowest_ind]:
            lowest_ind = i 
    return lowest_ind

        
v = [17,92,18,33,58, 7, 33, 42]
print(find_min(v))
print(find_min_ind(v))