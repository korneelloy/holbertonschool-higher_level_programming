#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
print(my_list)

idx = 5
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
