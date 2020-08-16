import re
total_hours = {}
with open("text_6.txt", encoding="utf-8") as file:

    for line in file.readlines():
        num_list = re.findall(r'\d+', line)
        sum = 0
        for i in num_list:
            sum += int(i)
        total_hours[line.split(":")[0]] = sum


print(total_hours)

