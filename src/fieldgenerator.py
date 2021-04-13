from random import randint

class FieldGenerator:
    def __init__(self, x:int, y:int, mines: int, first_click: tuple):
        self.x = x
        self.y = y
        self.mines = mines
        self.first_click = first_click

    def generate(self):
        horizontal = []
        matrix = []

        checks = [(-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        mine_checks = []
        for check in checks:
            mine_checks.append((self.first_click[0] + check[0], self.first_click[1] + check[1]))

        for i in range(self.x):
            horizontal.append(0)
        for i in range(self.y):
            matrix.append(horizontal.copy())

        for i in range(self.mines):
            mine_y = randint(0, self.y - 1)
            mine_x = randint(0, self.x - 1)

            while (mine_x, mine_y) in mine_checks:
                mine_y = randint(0, self.y - 1)
                mine_x = randint(0, self.x - 1)

            matrix[mine_y][mine_x] = -1

        for y in range(self.y):
            for x in range(self.x):
                if matrix[y][x] == -1:
                    continue
                n = 0

                for i in checks:

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