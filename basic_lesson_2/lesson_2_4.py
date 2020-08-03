string = input("Write numbers with space  ").split()

for n,i in enumerate(string, 1):
    print(n, i) if len(i) <= 10 else print(n, (i[:10]))