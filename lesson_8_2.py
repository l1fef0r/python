class DivisionByNull:
    @staticmethod
    def divide_by_null(div, denom):
        try:
            return (div / denom)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull()
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
