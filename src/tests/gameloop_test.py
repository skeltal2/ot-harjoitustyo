import unittest
import pygame
from gameloop import Gameloop

class TestGameloop(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.gameloop = Gameloop(None, 10, 10, 0, 36)

    def test_tile_can_be_opened(self):
        x = []
        
        for tile in self.gameloop.field.tiles:
            self.gameloop._open_tile((tile.rect.x, tile.rect.y))
            x.append(tile.style)

        self.assertEqual(x[0], "tile.png")