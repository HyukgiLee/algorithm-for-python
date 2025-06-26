# This program finds the duplicate names using set
# input : list of names with n entries(list)
# output : set of duplicate names(set)
def find_same_name_set(name_list):
    duplicates = set()
    seen = set()

    for name in name_list:
        if name not in seen:
            seen.add(name)
        else:
            duplicates.add(name)
    return duplicates


name = ['Tom', 'Jerry','Mike','Tom']
print(find_same_name_set(name))
name2 =  ['Tom', 'Jerry','Mike','Tom', 'Mike']
print(find_same_name_set(name2))