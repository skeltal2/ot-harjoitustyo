import os
import pygame

dirname = os.path.dirname(__file__)

class Tile(pygame.sprite.Sprite):
    def __init__(self, status: int, hidden: bool, x: int, y: int):
        super().__init__()

        if hidden:
            style = "tile2.png"
        else:
            if status == 0:
                style = "tile.png"
            elif status == -1:
                style = "mine.png"
            elif status == 1:
                style = "1.png"
            elif status == 2:
                style = "2.png"
            elif status == 3:
                style = "3.png"
            elif status == 4:
                style = "4.png"
            elif status == 5:
                style = "5.png"
            elif status == 6:
                style = "6.png"
            elif status == 7:
                style = "7.png"
            elif status == 8:
                style = "8.png"
            elif status == 9:
                style = "flag.png"

        self.image = pygame.image.load(os.path.join(dirname, "assets", style))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y