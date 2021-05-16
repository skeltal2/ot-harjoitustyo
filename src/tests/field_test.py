import unittest
from game.field import Field

class TestField(unittest.TestCase):
    def setUp(self):
        self.field_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.field = Field(self.field_map, 36)
    
    def test_tiles_initialize_correctly(self):
        self.assertEqual(self.field._initialize_sprites(self.field_map), True)