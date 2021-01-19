time = int(input("В одном дне 86400 секунд, введите число не больше 86400, чтобы получить текущее время  "))
if (time < 86400) :
    time_hours = time//3600
    time_minutes = time%3600//60
    time_seconds = time%3600%60
    print(f"{time_hours:0>2d} : {time_minutes:0>2d} : {time_seconds:0>2d}")
