from os import name
import tkinter as tk
import pygame
from gameloop import Gameloop
from high_scores import HighScores

class MainMenu:
    """Main menu and window for the game.

    """
    def __init__(self):
        """Initialize main menu.

        Args:
            field_x: Field width in tiles.
            field_y: Field heigh in tiles.
            mines: Amount of mines on the field.
            tile_size: Tile side lenght in pixels.
            tk_root: Main menu tkinter window
        """
        self.field_x = 16
        self.field_y = 16
        self.mines = 40
        self.tile_size = 36 # Should always be 36

        self.tk_root = tk.Tk()
        self.tk_root.title("Miinaharava")

        screen_x = (self.tk_root.winfo_screenwidth()/2) - (360/2)
        screen_y = (self.tk_root.winfo_screenheight()/2) - (240/2)

        self.tk_root.geometry(f"360x240+{int(screen_x)}+{int(screen_y)}") # Center window

        self.menu()
        self.tk_root.mainloop()


    def menu(self):
        """Set up buttons for main menu.

        """
        self.var = tk.IntVar(self.tk_root, 0)
        self.name_var = tk.StringVar(self.tk_root)

        heading_label = tk.Label(
            master=self.tk_root,
            text="Miinaharava",
        )
        start_button = tk.Button(
            master=self.tk_root,
            text="Uusi Peli",
            command=self.start_game,
        )
        diff_easy = tk.Radiobutton(
            master=self.tk_root,
            text="Helppo",
            variable=self.var,
            value=1
        )
        diff_medium = tk.Radiobutton(
            master=self.tk_root,
            text="Keskitaso",
            variable=self.var,
            value=2
        )
        diff_hard = tk.Radiobutton(
            master=self.tk_root,
            text="Vaikea",
            variable=self.var,
            value=3
        )
        name_field = tk.Entry(
            master=self.tk_root,
            textvariable=self.name_var
        )
        label = tk.Label(
            master=self.tk_root,
            text="Nimi:"
        )
        scores_button = tk.Button(
            master=self.tk_root,
            text="Tulokset",
            command=self.show_scores
        )
        quit_button = tk.Button(
            master=self.tk_root,
            text="Poistu",
            command=self._destroy
        )

        heading_label.grid(
            row=0, column=0, columnspan=3,
            sticky=(tk.constants.E, tk.constants.W),
            padx=5, pady=5
        )
        start_button.grid(
            row=1, column=1,
            sticky=(tk.constants.E, tk.constants.W),
            padx=5, pady=10
        )
        diff_easy.grid(
            row=3, column=0,
            padx=5, pady=5
        )
        diff_medium.grid(
            row=3, column=1,
            padx=5, pady=5
        )
        diff_hard.grid(
            row=3, column=2,
            padx=5, pady=5
        )
        name_field.grid(
            row=5, column=1,
            sticky=(tk.constants.E, tk.constants.W),
            padx=5, pady=10
        )
        label.grid(
            row=5, column=0
        )
        scores_button.grid(
            row=7, column=1,
            sticky=(tk.constants.E, tk.constants.W),
            padx=5, pady=10
        )
        quit_button.grid(
            row=9, column=1,
            sticky=(tk.constants.E, tk.constants.W),
            padx=5, pady=10
        )

        self.tk_root.grid_columnconfigure(1, weight=1)

    def _destroy(self):
        """Destroy tkinter window.

        """
        self.tk_root.destroy()

    def start_game(self):
        """Start game in new window.

        """
        self.name = self.name_var.get()
        self.tk_root.withdraw()
        self.make_window()

    def make_window(self):
        """Create window for new game.

        """
        self._find_difficulty(self.var)

        height = self.field_y
        width = self.field_x
        display_height = height * self.tile_size + self.tile_size
        display_width = width * self.tile_size

        display = pygame.display.set_mode((display_width, display_height))
        display.fill((0, 0, 0))

        pygame.display.set_caption("Miinaharava")

        pygame.init()
        
        if self.var.get() > 3 or len(self.name) < 1:
            use_score = False
        else:
            use_score = True

        Gameloop(display, self.field_x, self.field_y, self.mines, self.tile_size, (self.var.get(), self.name), use_score).start()

        pygame.display.quit()
        self.tk_root.deiconify()

    def show_scores(self):
        self.tk_root.withdraw()
        HighScores(self.tk_root)

    def _find_difficulty(self, var):
        """Set game difficulty for new game

        """
        if var.get() == 1:
            self.field_x = 9
            self.field_y = 9
            self.mines = 10
        elif var.get() == 2:
            self.field_x = 16
            self.field_y = 16
            self.mines = 40
        elif var.get() == 3:
            self.field_x = 30
            self.field_y = 16
            self.mines = 99
        else:
            self.field_x = 16
            self.field_y = 16
            self.mines = 40
        
        # MAX MINES: x * y - 9

if __name__ == "__main__":
    MainMenu()
