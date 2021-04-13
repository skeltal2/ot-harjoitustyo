import os
import pygame

dirname = os.path.dirname(__file__)

class Tile(pygame.sprite.Sprite):
    def __init__(self, status: int, x: int, y: int):
        super().__init__()
        self.status = status

        self.style = "tile2.png"
        self.image = pygame.image.load(os.path.join(dirname, "assets", self.style))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def click(self):
        if self.status == 0:
            self.style = "tile.png"
        elif self.status == -1:
            self.style = "mine.png"
        elif self.status == 1:
            self.style = "1.png"
        elif self.status == 2:
            self.style = "2.png"
        elif self.status == 3:
            self.style = "3.png"
        elif self.status == 4:
            self.style = "4.png"
        elif self.status == 5:
            self.style = "5.png"
        elif self.status == 6:
            self.style = "6.png"
        elif self.status == 7:
            self.style = "7.png"
        elif self.status == 8:
            self.style = "8.png"
        elif self.status == 9:
            self.style = "flag.png"

        self.image = pygame.image.load(os.path.join(dirname, "assets", self.style))

    # def flag(self):
    #     self.style = "flag.png"
    #     self.image = pygame.image.load(os.path.join(dirname, "assets", self.style))