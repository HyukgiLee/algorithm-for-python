# This program finds the person with the same name in the list
# input : a list with n name entries(list)
# output : set of duplicate names from the list (set)

def find_same_name(name_list):
    n = len(name_list)
    result = set()
    # 0 to n-1 (n-1 not n because last person doesn't need to compare himself)
    for i in range(0,n-1):
        # compare from current person(i) + 1 person
        for j in range(i+1, n):
            if name_list[i] == name_list[j]:
                result.add(name_list[i])
    return result

name = ['Tom', 'Jerry','Mike','Tom']
print(find_same_name(name))
name2 =  ['Tom', 'Jerry','Mike','Tom', 'Mike']
print(find_same_name(name2))