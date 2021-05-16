import unittest
import pygame
import random
from game.gameloop import Gameloop

class TestGameloop(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.gameloop = Gameloop(None, 10, 10, 0, 36, use_score=False)

    def test_tile_can_be_opened(self):
        # Pick a random tile and open it
        tile = random.choice(self.gameloop.field.tiles.sprites())
        self.gameloop._open_tile((tile.rect.x, tile.rect.y))
        self.assertEqual(tile.style, "tile.png")
    
    def test_tile_can_be_flagged(self):
        # Pick a random tile and flag it
        tile = random.choice(self.gameloop.field.tiles.sprites())
        self.gameloop._flags = 1
        self.gameloop._flag((tile.rect.x, tile.rect.y))
        self.assertEqual(tile.style, "flag.png")
    
    def test_tile_can_be_unflagged(self):
        tile = random.choice(self.gameloop.field.tiles.sprites())
        self.gameloop._flags = 1
        self.gameloop._flag((tile.rect.x, tile.rect.y))
        self.gameloop._flag((tile.rect.x, tile.rect.y))
        self.assertEqual(tile.style, "tile2.png")
    
    def test_game_state_game_over(self):
        # Pick a random tile, change it to a mine, then open it
        tile = random.choice(self.gameloop.field.tiles.sprites())
        tile.value = -1
        self.gameloop._open_tile((tile.rect.x, tile.rect.y))
        self.assertEqual(self.gameloop._game_state, -1)
    
    def test_game_state_game_won(self):
        # Pick a random tile, change it to a mine, then flag it
        tile = random.choice(self.gameloop.field.tiles.sprites())
        tile.value = -1
        self.gameloop.mines = 1
        self.gameloop._flags = 1
        self.gameloop._flag((tile.rect.x, tile.rect.y))
        self.assertEqual(self.gameloop._game_state, 10)
