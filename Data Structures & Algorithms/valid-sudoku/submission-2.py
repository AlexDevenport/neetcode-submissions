# Вам дана доска судоку размером 9х9. Доска судоку считается
# допустимой, если соблюдены следующие правила:

# - Каждая строка должна содержать цифры от 1 до 9 без повторений.
# - Каждый столбец должен содержать цифры от 1 до 9 без повторений.
# - Каждый из девяти подблоков сетки размером 3х3 должен содержать 
# цифры от 1 до 9 без повторений.
# - Верните true, если доска судоку допустима, в противном случае 
# верните false.

# Примечание: Доска не обязательно должна быть заполнена или решаема, 
# чтобы считаться допустимой.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Проверяем строки
        for row in board:
            seen = set()
            for num in row:
                if num in seen:
                    return False
                elif num.isdigit():
                    seen.add(num)

        # Проверяем столбцы
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num in seen:
                    return False
                elif num.isdigit():
                    seen.add(num)
    
        # Проверяем квадраты 3x3
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()

                for row in range(3):
                    for col in range(3):
                        num = board[box_row + row][box_col + col]

                        if num in seen:
                            return False
                        elif num.isdigit():
                            seen.add(num)

        return True