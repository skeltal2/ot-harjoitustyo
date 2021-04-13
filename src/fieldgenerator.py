from random import randint

class FieldGenerator:
    def __init__(self, x:int, y:int, mines: int):
        self.x = x
        self.y = y
        self.mines = mines

    def generate(self):
        horizontal = []
        matrix = []

        mine_checks = [(-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        for i in range(self.x):
            horizontal.append(0)
        for i in range(self.y):
            matrix.append(horizontal.copy())

        for i in range(self.mines):
            matrix[randint(0, self.y - 1)][randint(0, self.x - 1)] = -1

        for y in range(self.y):
            for x in range(self.x):
                if matrix[y][x] == -1:
                    continue
                n = 0

                for i in mine_checks:

                    y_check = y + i[1]
                    if y_check < 0 or y_check > self.y - 1:
                        continue

                    x_check = x + i[0]
                    if x_check < 0 or x_check > self.x - 1:
                        continue

                    if matrix[y_check][x_check] == -1:
                        n += 1
                matrix[y][x] = n
        
        return matrix