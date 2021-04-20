from random import sample
from math import floor

class FieldGenerator:
    def __init__(self, x:int, y:int, mines: int, first_click: tuple):
        self.field_x = x
        self.field_y = y
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

            if x_check < 0 or y_check < 0 or x_check > self.field_x or y_check > self.field_y:
                continue

            mine_checks.append((x_check, y_check))

        for i in range(self.field_x):
            horizontal.append(0)
        for i in range(self.field_y):
            matrix.append(horizontal.copy())

        for fc_y in range(self.field_y):
            for fc_x in range(self.field_x):
                if (fc_x, fc_y) not in mine_checks:
                    free_cords.add((fc_x, fc_y))

        for i in range(self.mines):
            mine_cord = sample(free_cords, 1)[0]

            matrix[mine_cord[1]][mine_cord[0]] = -1
            free_cords.remove((mine_cord[0], mine_cord[1]))

        for field_y in range(self.field_y):
            for field_x in range(self.field_x):
                if matrix[field_y][field_x] == -1:
                    continue
                tile_value = 0

                for i in checks:
                    y_check = field_y + i[1]
                    if y_check < 0 or y_check > self.field_y - 1:
                        continue

                    x_check = field_x + i[0]
                    if x_check < 0 or x_check > self.field_x - 1:
                        continue

                    if matrix[y_check][x_check] == -1:
                        tile_value += 1
                matrix[field_y][field_x] = tile_value
        return matrix

    def __str__(self):
        return f"x:{self.field_x}, y:{self.field_y}, mines:{self.mines}"
