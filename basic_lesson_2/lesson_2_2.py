print("Please write any items to fill list, when you finish add items to write END")
list_items = []
while(True):
    item = input("Write item here:  ")
    if(item == "end"): break
    list_items.append(item)

print(list_items)

i = 0

while(i + 1 < len(list_items)):
        list_items[i], list_items[i+1] = list_items[i+1], list_items[i]
        i += 2

print(list_items)



