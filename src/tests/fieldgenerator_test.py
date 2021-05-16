import unittest
from game.fieldgenerator import FieldGenerator

class TestFieldGenerator(unittest.TestCase):
    def test_field_generator_generates_properly(self):
        field = FieldGenerator(5, 5, 0, (-10, -10)).generate()
        self.assertEqual(field, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_field_generator_generates_mines(self):
        field = FieldGenerator(5, 5, 5, (-10, -10)).generate()
        n = 0

        for i in field:
            for x in i:
                if x == -1:
                    n += 1
        
        self.assertEqual(5, n)