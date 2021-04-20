import pygame
import os
from gameloop import Gameloop

x = 10
y = 10
mines = 10
tile_size = 36

def main():
    height = y
    width = x
    display_height = height * tile_size + tile_size
    display_width = width * tile_size

    display = pygame.display.set_mode((display_width, display_height))
    display.fill((0, 0, 0))

    pygame.display.set_caption("Minesweeper")

    pygame.init()

    Gameloop(display, x, y, mines, tile_size).start()

if __name__ == "__main__":
    main()