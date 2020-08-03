my_list = [7, 5, 3, 3, 2]
while True:
    print(f"Current rating  {my_list}")
    item = input("Write the number or end to finish ")
    if item == "end": break
    if item.isdigit():
        item = int(item)
        if my_list.count(item):
            my_list.insert(my_list.index(item) + my_list.count(item), item)
        else:
            param = 0
            i_param = 0
            for i, it in enumerate(my_list):
                if item > it:
                    i_param = i
                    param = item
                    if((item - it) != 0):
                        break
                else:
                    i_param = i + 1
                    param = item

            my_list.insert(i_param, param)

    elif not item.isdigit():
        print("Write the number")
    else: break