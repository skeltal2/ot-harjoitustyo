import pygame
from game.tile import Tile

class Field:
    """Object to contain tile objects.

    Attributes:
        tile_size: Lenght of tile side in pixels.
        tiles: Sprite group of tiles.
    """
    def __init__(self, field_map: list, tile_size: int):
        """Initialize Field object

        Args:
            field_map: Matrix with tile locations and styles.
            tile_size: Lenght of tile side in pixels.
        """
        self.tile_size = tile_size
        self.tiles = pygame.sprite.Group()

        self._initialize_sprites(field_map)

    def _initialize_sprites(self, field_map):
        height = len(field_map)
        width = len(field_map[0])

        for map_y in range(height):
            for map_x in range(width):
                value = field_map[map_y][map_x]
                norm_x = map_x * self.tile_size
                norm_y = map_y * self.tile_size + self.tile_size

                self.tiles.add(Tile(value, norm_x, norm_y))
