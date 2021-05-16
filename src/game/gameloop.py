import sqlite3
import pygame
from game.fieldgenerator import FieldGenerator
from game.field import Field

class Gameloop:
    """Class contains main gameloop for running the game itself.

    Attributes:
        field_x: Field width in tiles.
        field_y: Field height in tiles.
        mines: Amount of mines on the field.
        tile_size: Lenght of a tiles side in pixels.
        field_map: Matrix which determines spirtes tiles use.
        field: Stores sprites.
    """
    def __init__(
            self, display, x: int, y: int, mines: int,
            data: tuple, use_score: bool
        ):
        """Initialize gameloop.

        Args:
            x: Field width in tiles.
            y: Field height in tiles.
            mines: Amount of mines on the field.
            data: Game difficulty and player name for database.
            use_score: Save score after game.
        """
        self.field_x = x
        self.field_y = y
        self.mines = mines
        self.tile_size = 36 # Should always be 36

        # Generate dummy field to show before first click
        self.field_map = FieldGenerator(self.field_x, self.field_y, 0, (0, 0)).generate()
        self.field = Field(self.field_map, self.tile_size)

        self._game_state = 0 # Game state: -1 Game over, 10 Game won, 0 Game in progress
        self._flagged_mines = 0
        self._flags = mines # Flags player can use
        self._font = pygame.font.SysFont("Calibri", 32)

        # Database for scores
        self._database = sqlite3.connect("src/database/scores.db")
        # Create table for first run
        self._database.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY,
                score INTEGER,
                mode INTEGER,
                name TEXT
            );
            """)
        self._database.commit()
        self._data = data
        self._use_score = use_score

        self._start_time = 0
        self._time = 0
        self._first_time = True
        self._clock = pygame.time.Clock()
        self._display = display

    def start(self):
        """Start the game.

        """
        self._start_time = pygame.time.get_ticks()
        while True:
            if self._events() is False:
                break
            self._render()
            self._clock.tick(60)
        if self._game_state == 10 and self._use_score:
            self._save_score(self._time)

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONUP:
                # After game over next click exists game
                if self._game_state != 0:
                    return False

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

    def _render(self):
        if self._game_state == -1:
            color = (255, 0, 0)
        elif self._game_state == 10:
            color = (0, 255, 0)
        else:
            self._time = pygame.time.get_ticks() - self._start_time
            color = (255, 255, 255)

        self._display.fill((0, 0, 0))

        # Draw tiles
        self.field.tiles.draw(self._display)

        # Show number of flags
        flg = self._font.render(f"{self._flags}", True, color)
        self._display.blit(flg, flg.get_rect())

        # Covert to minutes and seconds
        seconds = "0" + str(int((self._time/1000)%60))
        minutes = "0" + str(int((self._time/(1000*60))%60))

        # Draw timer
        time = self._font.render(f"{minutes[-2:]}:{seconds[-2:]}", True, color)
        self._display.blit(time, ((self._display.get_width() / 2) - (time.get_width() / 2), 0))

        pygame.display.flip()
        pygame.display.update()

    def _open_tile(self, position):
        if self._game_state == 0: # Check if game in progress
            for tile in self.field.tiles:
                # Iterate through all tiles and check if any tile collides with clicked position,
                # then try to open tile.
                # Break loop when tile is found
                if tile.rect.collidepoint(position):
                    if tile.style == "flag.png": # Flagged tiles cannot be opened
                        break
                    if tile.value == 0: # If empty tile, also open all surrounding tiles
                        cords = []
                        for i in [
                            (-36, 36), (0, 36), (36, 36), (-36, 0),
                            (36, 0), (-36, -36), (0, -36), (36, -36)]:
                            cords.append((tile.rect.x + i[0], tile.rect.y + i[1]))
                        self._update_game_state(tile.click()) # Update game_state for clicked tile

                        for tile2 in self.field.tiles:
                            if (tile2.rect.x, tile2.rect.y) in cords:
                                if tile2.value != 0 and tile2.style != "flag.png":
                                    tile2.click()
                                # If any surrounding tile is empty, also open its surrounding tiles
                                elif tile2.style == "tile2.png":
                                    tile2.click()
                                    self._open_tile((tile2.rect.x, tile2.rect.y))
                        break
                    # Else, open tile and update game_state
                    self._update_game_state(tile.click())
                    break

    def _flag(self, position):
        if self._game_state == 0:
            for tile in self.field.tiles:
                if tile.rect.collidepoint(position):
                    # If tile is not flagged, flag it and update flag count
                    if tile.style == "tile2.png" and self._flags > 0:
                        self._flags -= 1
                        if tile.flag() == -1:
                            self._flagged_mines += 1
                            self._update_game_state(9)
                        return tile
                    # If tile is flagged, remove flag and update flag count
                    elif tile.style == "flag.png":
                        self._flags += 1
                        if tile.unflag() == -1:
                            self._flagged_mines -= 1
                            self._update_game_state(9)
                        return tile

    def _update_game_state(self, value):
        # If mine was clicked, set game_state to game over (-1)
        if value == -1:
            self._game_state = -1
        # If all mines are flagged, set game_state to game won (10)
        elif self._flagged_mines == self.mines:
            self._game_state = 10
        else:
            self._game_state = 0

    def _save_score(self, score: int):
        mode = self._data[0]
        name = self._data[1]

        self._database.execute(
                "INSERT INTO scores (score, mode, name) VALUES (?, ?, ?)",
                (score, mode, name)
            )
        self._database.commit()
