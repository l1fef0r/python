list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [num for num in range (1, len(list)) if list.count(num) == 1]
print(new_list)