import pygame
from fieldgenerator import FieldGenerator
from field import Field

class Gameloop:
    def __init__(self, display, x, y, mines, tile_size):
        self.field_x = x
        self.field_y = y
        self.mines = mines
        self.tile_size = tile_size

        # Generate dummy field to show before first click
        self.field_map = FieldGenerator(self.field_x, self.field_y, 0, (0, 0)).generate()
        self.field = Field(self.field_map, self.tile_size)

        self.game_state = 0 # Game state: -1 Game over, 10 Game won, 0 Game in progress
        self.flagged_mines = 0
        self.flags = mines # Flags player can use
        self.font = pygame.font.SysFont("Calibri", 36)

        self._first_time = True
        self._clock = pygame.time.Clock()
        self._display = display

    def start(self):
        while True:
            if self._events() is False:
                break

            self._render()
            self._clock.tick(60)

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # Generate real field after first click
                if self._first_time:
                    self.field_map = FieldGenerator(
                        self.field_x, self.field_y, self.mines, (pos[0], pos[1] - self.tile_size)
                        ).generate()
                    self.field = Field(self.field_map, self.tile_size)
                    self._first_time = False

                # Open tile (left mouse)
                if event.button == 1:
                    self._open_tile(pos)

                # Place flag (right mouse)
                elif event.button == 3:
                    self._flag(pos)
            else:
                pass

    def _render(self):
        if self.game_state == -1:
            text = "Hävisit pelin"
        elif self.game_state == 10:
            text = "Voitit pelin"
        else:
            text = ""

        self._display.fill((0, 0, 0))

        self.field.tiles.draw(self._display)

        # Show text in top right
        end = self.font.render(text, True, (255, 255, 255))
        self._display.blit(end, (self._display.get_width() - end.get_width(), 0))

        # Show number of flags
        flg = self.font.render(f"{self.flags}", True, (255, 255, 255))
        self._display.blit(flg, flg.get_rect())

        pygame.display.flip()
        pygame.display.update()

    def _open_tile(self, position):
        if self.game_state == 0: # Check if game in progress
            for tile in self.field.tiles:
                # Iterate through all tiles and check if any tile collides with clicked position, then try to open tile. 
                # Break loop when tile is found
                if tile.rect.collidepoint(position): 
                    if tile.style == "flag.png": # Flagged tiles cannot be opened
                        break
                    elif tile.value == 0: # If empty tile, also open all surrounding tiles
                        cords = []
                        for i in [
                            (-36, 36), (0, 36), (36, 36), (-36, 0),
                            (36, 0), (-36, -36), (0, -36), (36, -36)]:
                            cords.append((tile.rect.x + i[0], tile.rect.y + i[1]))
                        self._game_state(tile.click()) # Update game_state for clicked tile

                        for tile2 in self.field.tiles:
                            if (tile2.rect.x, tile2.rect.y) in cords:
                                if tile2.value != 0 and tile2.style != "flag.png":
                                    tile2.click()
                                elif tile2.style == "tile2.png": # If any surrounding tile is empty, also open its surrounding tiles
                                    tile2.click()
                                    self._open_tile((tile2.rect.x, tile2.rect.y))
                        break
                    else: # Else, open tile and update game_state
                        self._game_state(tile.click())
                        break
    
    def _flag(self, position):
        if self.game_state == 0:
            for tile in self.field.tiles:
                if tile.rect.collidepoint(position):
                    # If tile is not flagged, flag it and update flag count
                    if tile.style == "tile2.png" and self.flags > 0:
                        self.flags -= 1
                        if tile.flag() == -1:
                            self.flagged_mines += 1
                            self._game_state(9)
                    # If tile is flagged, remove flag and update flag count
                    elif tile.style == "flag.png":
                        self.flags += 1
                        if tile.unflag() == -1:
                            self.flagged_mines -= 1
                            self._game_state(9)

    def _game_state(self, value):
        # If mine was clicked, set game_state to game over (-1)
        if value == -1:
            self.game_state = -1
        # If all mines are flagged, set game_state to game won (10)
        elif self.flagged_mines == self.mines:
            self.game_state = 10
        else:
            self.game_state = 0
