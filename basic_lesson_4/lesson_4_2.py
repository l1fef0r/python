list = [10, 20, 30, 3, 4, 776,6, 88, 6, 7, 88, 7]
new_list = [list[num] for num in range (1, len(list)) if list[num] > list[num-1]]
print(new_list)
