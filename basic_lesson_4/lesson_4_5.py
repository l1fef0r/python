from functools import reduce
def refuce_func(el_prev, el):
    return  el_prev * el
new_list = [num for num in range (100, 1001) if (num%2 == 0)]
print(f"Строка с умноженными элементами списка\n {reduce(refuce_func, new_list)}")
