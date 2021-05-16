import unittest
from game.tile import Tile

class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile(-1, 0, 0)
    
    def test_tile_can_be_clicked(self):
        self.tile.click()
        self.assertEqual(self.tile.style, "mine.png")
    
    def test_tile_can_be_flagged(self):
        self.tile.flag()
        self.assertEqual(self.tile.style, "flag.png")
    
    def test_tile_can_be_unflagged(self):
        self.tile.unflag()
        self.assertEqual(self.tile.style, "tile2.png")

    def test_tile_style_click_0(self):
        tile = Tile(0, 0, 0)
        self.assertEqual(tile.click(), 0)

    def test_tile_style_click_1(self):
        tile = Tile(1, 0, 0)
        self.assertEqual(tile.click(), 1)

    def test_tile_style_click_2(self):
        tile = Tile(2, 0, 0)
        self.assertEqual(tile.click(), 2)

    def test_tile_style_click_3(self):
        tile = Tile(3, 0, 0)
        self.assertEqual(tile.click(), 3)

    def test_tile_style_click_4(self):
        tile = Tile(4, 0, 0)
        self.assertEqual(tile.click(), 4)
    
    def test_tile_style_click_5(self):
        tile = Tile(5, 0, 0)
        self.assertEqual(tile.click(), 5)
    
    def test_tile_style_click_6(self):
        tile = Tile(6, 0, 0)
        self.assertEqual(tile.click(), 6)
    
    def test_tile_style_click_7(self):
        tile = Tile(7, 0, 0)
        self.assertEqual(tile.click(), 7)
    
    def test_tile_style_click_8(self):
        tile = Tile(8, 0, 0)
        self.assertEqual(tile.click(), 8)
    
    def test_tile_style_click_9(self):
        tile = Tile(9, 0, 0)
        self.assertEqual(tile.click(), 9)
    
    def test_tile_style_click_non_valid_value(self):
        tile = Tile("test", 0, 0)
        self.assertEqual(tile.click(), 0)