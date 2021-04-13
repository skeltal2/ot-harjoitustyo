import pygame
from fieldgenerator import FieldGenerator

class Gameloop:
    def __init__(self, display, field, field_map):
        self._field = field
        self._field_map = field_map
        self._clock = pygame.time.Clock()
        self._display = display

    def start(self):
        while True:
            if self._events() == False:
                break

            self._render()
            self._clock.tick(60)
    
    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.open_tile(pos)

    def _render(self):
        self._field.tiles.draw(self._display)
        pygame.display.update()

    def open_tile(self, position):
        for tile in self._field.tiles:
            if tile.rect.collidepoint(position):
                if tile.status == 0:
                    cords = []
                    for i in [(-36, 36), (0, 36), (36, 36), (-36, 0), (0, 0), (36, 0), (-36, -36), (0, -36), (36, -36)]:
                        cords.append((tile.rect.x + i[0], tile.rect.y + i[1]))

                    for tile2 in self._field.tiles:
                        if (tile2.rect.x, tile2.rect.y) in cords:
                            if tile2.status != 0:
                                tile2.click()
                            else:
                                if tile2.style == "tile2.png":
                                    tile2.click()
                                    self.open_tile((tile2.rect.x, tile2.rect.y))
                else:
                    tile.click()