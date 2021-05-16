import os
import pygame

dirname = os.path.dirname(__file__)

class Tile(pygame.sprite.Sprite):
    """Tile object.

    Attributes:
        value: Type of tile (from -1 to 9)
        style: Name of sprite file.
        image: Sprite file.
        rect: Rect collider
    """
    def __init__(self, value: int, tile_x: int, tile_y: int):
        """Initialize tile.

        Args:
            value: Type of tile (-1: mine, 0: empty, 1 - 8: number, 9: flag).
            tile_x: X cordinate.
            tile_y: Y cordinate.
        """
        super().__init__()
        self.value = value

        self.style = "tile2.png"
        self.image = pygame.image.load(os.path.join(dirname, "../assets", self.style))

        self.rect = self.image.get_rect()

        self.rect.x = tile_x
        self.rect.y = tile_y

    def _set_image(self, style):
        self.image = pygame.image.load(os.path.join(dirname, "../assets", style))

    # When tile is clicked assing correct sprite
    def click(self):
        """Change sprite from hidden to sprite that matches tile's type.

        Returns:
            value: Tile's type
        """
        if self.value == 0:
            self.style = "tile.png"
        elif self.value == -1:
            self.style = "mine.png"
        elif self.value == 1:
            self.style = "1.png"
        elif self.value == 2:
            self.style = "2.png"
        elif self.value == 3:
            self.style = "3.png"
        elif self.value == 4:
            self.style = "4.png"
        elif self.value == 5:
            self.style = "5.png"
        elif self.value == 6:
            self.style = "6.png"
        elif self.value == 7:
            self.style = "7.png"
        elif self.value == 8:
            self.style = "8.png"
        elif self.value == 9:
            self.style = "flag.png"
        else:
            self.value = 0
            self.style = "tile.png"

        self._set_image(self.style)

        return self.value

    def flag(self):
        """Change tile to flagged tile.

        Returns:
            value: Tile's value
        """
        self.style = "flag.png"
        self._set_image(self.style)

        return self.value

    def unflag(self):
        """Change tile to hidden tile.

        Returns:
            value: Tile's value
        """
        self.style = "tile2.png"
        self._set_image(self.style)

        return self.value
