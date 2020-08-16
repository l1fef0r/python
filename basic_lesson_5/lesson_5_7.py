import json
result = []

with open("text_7.json", "w", encoding="utf-8") as jfile:
    profit = {}
    with open("text_7.txt", encoding="utf-8") as file:

        for line in file.readlines():
            firm = line.split()
            profit[firm[0]] = int(firm[2]) - int(firm[3])

        profit_in_plus = [int(i) for i in profit.values() if int(i) > 0]
        average_profit = round(sum(profit_in_plus)/len(profit_in_plus))

        result.append(profit)
        result.append({"average_profit": average_profit})

    json.dump(result, jfile)