import pygame
from fieldgenerator import FieldGenerator
from field import Field

class Gameloop:
    def __init__(self, display, x, y, mines, tile_size):
        self.x = x
        self.y = y
        self.mines = mines
        self.tile_size = tile_size

        self.field_map = FieldGenerator(self.x, self.y, 0, (0, 0)).generate()
        self.field = Field(self.field_map, self.tile_size)

        self.game_state = 0
        self.flagged_mines = 0
        self.flags = mines
        self.font = pygame.font.SysFont("Calibri", 36)

        self._first_time = True
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

                if self._first_time:
                    self.field_map = FieldGenerator(self.x, self.y, self.mines, pos).generate()
                    self.field = Field(self.field_map, self.tile_size)
                    self._first_time = False

                if event.button == 1:
                    self._open_tile(pos)

                elif event.button == 3:
                    self._flag(pos)

    def _render(self):
        if self.game_state == -1:
            text = "Hävisit pelin"
        elif self.game_state == 10:
            text = "Voitit pelin"
        else:
            text = ""

        self._display.fill((0, 0, 0))

        self.field.tiles.draw(self._display)

        cond = self.font.render(text, True, (255, 255, 255))
        self._display.blit(cond, (self._display.get_width() - cond.get_width(), 0))

        score = self.font.render(f"{self.flags}", True, (255, 255, 255))
        self._display.blit(score, score.get_rect())

        pygame.display.flip()
        pygame.display.update()

    def _open_tile(self, position):
        if self.game_state == 0:
            for tile in self.field.tiles:
                if tile.rect.collidepoint(position):
                    if tile.style == "flag.png":
                        break
                    elif tile.status == 0:
                        cords = []
                        for i in [(-36, 36), (0, 36), (36, 36), (-36, 0), (36, 0), (-36, -36), (0, -36), (36, -36)]:
                            cords.append((tile.rect.x + i[0], tile.rect.y + i[1]))
                        
                        self._game_state(tile.click())

                        for tile2 in self.field.tiles:
                            if (tile2.rect.x, tile2.rect.y) in cords:
                                if tile2.status != 0 and tile2.style != "flag.png":
                                    tile2.click()
                                elif tile2.style == "tile2.png":
                                    tile2.click()
                                    self._open_tile((tile2.rect.x, tile2.rect.y))
                        break
                    elif tile.style != "flag.png":
                        self._game_state(tile.click())
                        break
                    else:
                        break
    
    def _flag(self, position):
        if self.game_state == 0:
            for tile in self.field.tiles:
                if tile.rect.collidepoint(position):
                    if tile.style == "tile2.png" and self.flags > 0:
                        self.flags -= 1
                        if tile.flag() == -1:
                            self.flagged_mines += 1
                            self._game_state(9)
                    elif tile.style == "flag.png":
                        self.flags += 1
                        if tile.unflag() == -1:
                            self.flagged_mines -= 1
                            self._game_state(9)

    def _game_state(self, n):
        if n == -1:
            self.game_state = -1
        elif self.flagged_mines == self.mines:
            self.game_state = 10
        else:
            self.game_state = 0