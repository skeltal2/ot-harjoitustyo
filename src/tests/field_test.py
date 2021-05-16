import unittest
from game.field import Field

class TestField(unittest.TestCase):
    def setUp(self):
        self.field_map = [[1, 1, 1], [1, -1, 1], [1, 1, 1]]
        self.field = Field(self.field_map, 36)
    
    def test_tiles_initialize_correctly(self):
        numbers = 0
        mines = 0

        for tile in self.field.tiles:
            if tile.value == -1:
                mines += 1
            elif tile.value > 0 and tile.value < 9:
                numbers += 1
        
        self.assertEqual((numbers, mines), (8, 1))