# Task 1
# group the elements of an input list of integers into groups of 3 values
# input: a list of integers
# output: a list of lists of 3 integers
def groups_of_3(integer_list:list[int]) -> list[list[int]]:
    groups_of_3_list = []
    len_groups_of_3_list = len(integer_list) // 3 + 1
    for i in range(len_groups_of_3_list):
        j = i*3
        sublist = [integer_list[j], integer_list[j+1], integer_list[j+2]]
        groups_of_3_list.append(sublist)
    return groups_of_3_list
