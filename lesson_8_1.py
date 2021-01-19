class Data:
    def __init__(self, d_m_y):

        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        my_date = []

        for i in d_m_y.split('-'):
            my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return f'Корректно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.d_m_y)}'


today = Data('11-1-2000')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11-11-2012'))
print(today.extract('11-11-2021'))
print(Data.valid(1, 11, 2000))
