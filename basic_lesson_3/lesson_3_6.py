import re
def int_func(word = "test"):
    return word.capitalize()


words = input("Введите любое количество слов через пробел ").lower()
print("to Lower\n" + words)

new_words = ""
for i in words:
    if(re.search('[qwertyuiopasdfghjklzxcvbnm ]', i)):
        new_words = new_words + i

words = new_words.lstrip()
print("\nOnly latin letters at now\n" + words)
list_word = words.split()
words = ""
for i in list_word:
    words = words + " " + int_func(i) #Замена всех слов в исходной переменной

print("\nto Upper any word \n" + words.lstrip())
