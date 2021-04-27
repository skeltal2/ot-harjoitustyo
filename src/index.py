import pygame
from gameloop import Gameloop
from mainmenu import MainMenu

X = 16
Y = 16
# max mines = x * y - 9
MINES = 40
TILE_SIZE = 36

def main_no_main_menu():
    height = X
    width = Y
    display_height = height * TILE_SIZE + TILE_SIZE
    display_width = width * TILE_SIZE

    display = pygame.display.set_mode((display_width, display_height))
    display.fill((0, 0, 0))

    pygame.display.set_caption("Miinaharava")

    pygame.init()

    Gameloop(display, X, Y, MINES, TILE_SIZE).start()

    pygame.display.quit()

def main():
    MainMenu()

if __name__ == "__main__":
    main()
    # main_no_main_menu()