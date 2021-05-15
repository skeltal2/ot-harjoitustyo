from random import sample
from math import floor

class FieldGenerator:
    """Class used to generate fields.

    Attributes:
        x: Horizontal tiles.
        y: Vertical tiles.
        mines: Amount of mines.
        first_click: Cordinates of first click
    """
    def __init__(self, x: int, y: int, mines: int, first_click: tuple):
        """Initialize field generator.

        Args:
            field_x: Horizontal tiles.
            field_y: Vertical tile.
            mines: Amount of mines.
            first_clikc: Cordinates of first click
        """
        self.field_x = x
        self.field_y = y
        self.mines = mines
        self.first_click = first_click

    def generate(self):
        """Returns a field.

        Returns:
            X by Y matrix with mines based on initialized values.
        """
        horizontal = []
        matrix = []
        free_cords = set() # List of cordinates where mines can be placed

        # Relative cordinates of all 8 surrounding tiles of a tile
        checks = [(-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        # Find 8 tiles which surround first tile clicked
        mine_checks = []
        for check in checks:
            x_check = floor(self.first_click[0] / 36) + check[0]
            y_check = floor(self.first_click[1] / 36) + check[1]

            if x_check < 0 or y_check < 0 or x_check > self.field_x or y_check > self.field_y:
                continue

            mine_checks.append((x_check, y_check))

        # Create x * y matrix
        matrix = self._create_matrix(self.field_x, self.field_y)

        # Add possible mine cordinates to free_cords
        for fc_y in range(self.field_y):
            for fc_x in range(self.field_x):
                if (fc_x, fc_y) not in mine_checks:
                    free_cords.add((fc_x, fc_y))

        # Pick a random cordinate from free_cords, add mine (-1) to matrix, then remove cordinate
        for i in range(self.mines):
            mine_cord = tuple(sample(free_cords, 1)[0])

            matrix[mine_cord[1]][mine_cord[0]] = -1
            free_cords.remove((mine_cord[0], mine_cord[1]))

        # Go through every tile and find count of surrounding mines
        for field_y in range(self.field_y):
            for field_x in range(self.field_x):
                if matrix[field_y][field_x] == -1:
                    continue
                tile_value = 0

                for i in checks: # Make sure numbers don't wrap around the field
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

    def _create_matrix(self, horizontal: int, vertical: int):
        """Create empty X by Y matrix.

        Args:
            horizontal: Matrix width.
            vertical: Matrix height.

        Returns:
            Empty X by Y matrix.
        """
        line = []
        matrix = []
        for i in range(horizontal):
            line.append(0)
        for i in range(vertical):
            matrix.append(line.copy())
        return matrix
