# 304. Range sum query 2D - Immutable

# Учитывая двумерную матрицу matrix, обработайте несколько запросов следующего типа:

# Вычислите сумму элементов матрицы внутри прямоугольника, определяемого 
# его верхним левым углом (row1, col1) и нижним правым углом (row2, col2).
# Реализуйте класс NumMatrix:

# NumMatrix(int[][] матрица) Инициализирует объект с помощью целочисленной матрицы matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Возвращает сумму элементов матрицы 
# внутри прямоугольника, определяемую его верхним левым углом (row1, col1) 
# и нижним правым углом (row2, col2).
# Вы должны разработать алгоритм, в котором sumRegion работает с O(1) временной сложностью.

'''
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2],
   [5, 6, 3, 2, 1],
   [1, 2, 0, 1, 5],
   [4, 1, 0, 1, 7],
   [1, 0, 3, 0, 5]]],
   [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]
'''

class NumMatrix:
    # time: O(m*n)
    # mem:  O(m*n)
    def __init__(self, matrix: List[List[int]]):
        # вторая матрица из нулей на 1 больше размера исходной
        # по горизонтали и вертикали
        rows = len(matrix)
        cols = len(matrix[0])

        prefixSum = [
            [0 for num in range(cols + 1)]
            for row in range(rows + 1)
        ]
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                # prefixSum[i][j] = prefixSum[i][j-1] + prefixSum[i-1][j] - prefixSum[i-1][j-1] + matrix[i-1][j-1]
                # matrix - оригинальный массив
                prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + matrix[i-1][j-1]
                
        self.prefixSum = prefixSum

        print('Матрица с префиксными суммами')
        for i in range(rows + 1):
            print(prefixSum[i])

    # time: O(1)
    # mem:  O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row2 += 1
        col2 += 1
        # ans = prefixSum[row2][col2] - prefixSum[row2][col1] - prefixSum[row2][col2] + prefixSum[row1][col1]
        try:
            return self.prefixSum[row2][col2] - self.prefixSum[row1][col2] - self.prefixSum[row2][col1] + self.prefixSum[row1][col1]
        except:
            raise IndexError('В функцию введены неправильные индексы в row и col')


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)