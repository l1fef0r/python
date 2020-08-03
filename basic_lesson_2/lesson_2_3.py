month = 0
while(True):
    month = input("Write the month number ")
    if(month.isdigit()):
        if(0 < int(month) < 13):
            break
        else:
            print("a month number must be from 1 to 12")
    else:
        print("It's not a digit")

month_list= ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

print(f"{month_list[int(month)]} {type(month_list)}")
print(f"{month_dict[int(month)]} {type(month_dict)}")

