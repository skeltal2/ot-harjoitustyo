import os
import pygame

dirname = os.path.dirname(__file__)

class Tile(pygame.sprite.Sprite):
    def __init__(self, value: int, x: int, y: int):
        super().__init__()
        self.value = value

        self.style = "tile2.png"
        self.image = pygame.image.load(os.path.join(dirname, "assets", self.style))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def set_image(self, style):
        self.image = pygame.image.load(os.path.join(dirname, "assets", style))

    # When tile is clicked assing correct sprite
    def click(self):
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

        self.set_image(self.style)

        return self.value

    def flag(self):
        self.style = "flag.png"
        self.set_image(self.style)

        return self.value

    def unflag(self):
        self.style = "tile2.png"
        self.set_image(self.style)

        return self.value