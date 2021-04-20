from random import randint, sample
from math import floor

class FieldGenerator:
    def __init__(self, x:int, y:int, mines: int, first_click: tuple):
        self.x = x
        self.y = y
        self.mines = mines
        self.first_click = first_click

    def generate(self):
        horizontal = []
        matrix = []
        free_cords = set()

        checks = [(-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        mine_checks = []
        for check in checks:
            x_check = floor(self.first_click[0] / 36) + check[0]
            y_check = floor(self.first_click[1] / 36) + check[1]

            if x_check < 0 or y_check < 0 or x_check > self.x or y_check > self.y:
                continue

            mine_checks.append((x_check, y_check))

        for i in range(self.x):
            horizontal.append(0)
        for i in range(self.y):
            matrix.append(horizontal.copy())

        for fc_y in range(self.y):
            for fc_x in range(self.x):
                if (fc_x, fc_y) not in mine_checks:
                    free_cords.add((fc_x, fc_y))

        for i in range(self.mines):
            mine_cord = sample(free_cords, 1)[0]

            matrix[mine_cord[1]][mine_cord[0]] = -1
            free_cords.remove((mine_cord[0], mine_cord[1]))

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

    def __str__(self):
        return f"x:{self.x}, y:{self.y}, mines:{self.mines}"