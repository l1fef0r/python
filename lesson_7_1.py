class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        str_m = ""
        for line in self.matrix:
            for el in line:
                str_m += str(el)
                str_m += "\t"
            str_m += '\n'

        return str_m

    def __add__(self, other):
          try:
              i = 0

              for line in self.matrix:
                ii = 0
                for el in line:
                    self.matrix[i][ii] = int(el) + int(other.matrix[i][ii])
                    ii += 1
                i += 1
              return Matrix(self.matrix)
          except:
              return "ошибка"



matrix = Matrix([[1,2,3], [10,20,30], [100,200,300]])
matrix2 = Matrix([[1, 2, 3], [10, 20, 30], [100, 200, 300]])
newM = matrix + matrix2

print(newM)
