d_e_list = [1, 2.0, "test", True, None, [1, 2], (1, 2)]
print(d_e_list)
for i, item in enumerate (d_e_list, 1):
    print(f"{i} {item} {type(item)}")