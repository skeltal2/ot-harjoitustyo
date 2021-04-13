import pygame
import os
from field import Field
from fieldgenerator import FieldGenerator

field_map = FieldGenerator(30, 16, 99).generate()

tile_size = 36

def main():
    height = len(field_map)
    width = len(field_map[0])
    display_height = height * tile_size
    display_width = width * tile_size

    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Minesweeper")

    field = Field(field_map, tile_size)

    pygame.init()

    field.tiles.draw(display)
    pygame.display.flip()

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

if __name__ == "__main__":
    main()