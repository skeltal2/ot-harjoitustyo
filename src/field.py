import pygame
from tile import Tile

class Field:
    def __init__(self, field_map, tile_size):
        self.tile_size = tile_size
        self.tiles = pygame.sprite.Group()

        self._initialize_sprites(field_map)

    def _initialize_sprites(self, field_map):
        height = len(field_map)
        width = len(field_map[0])

        for y in range(height):
            for x in range(width):
                n = field_map[y][x]
                norm_x = x * self.tile_size
                norm_y = y * self.tile_size

                self.tiles.add(Tile(n, norm_x, norm_y))