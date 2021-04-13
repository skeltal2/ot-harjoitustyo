import unittest
from fieldgenerator import FieldGenerator

class TestFieldGenerator(unittest.TestCase):
    def setUp(self):
        self.field = FieldGenerator(10, 10, 10, (0, 0))

    def test_field_dimensions(self):
        field = str(self.field)
        self.assertEqual(field, "x:10, y:10, mines:10")