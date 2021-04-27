import tkinter as tk
import pygame
from gameloop import Gameloop

class MainMenu:
    def __init__(self):
        self.field_x = 16
        self.field_y = 16
        self.mines = 40
        self.tile_size = 36

        self.tk_root = tk.Tk()

        screen_x = (self.tk_root.winfo_screenwidth()/2) - (360/2)
        screen_y = (self.tk_root.winfo_screenheight()/2) - (240/2)

        self.tk_root.geometry(f"360x240+{int(screeen_x)}+{int(screen_y)}")

        self.menu()
        self.tk_root.mainloop()


    def menu(self):
        self.var = tk.IntVar(self.tk_root, 0)

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
        quit_button = tk.Button(
            master=self.tk_root,
            text="Poistu",
            command=self.destroy
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
        quit_button.grid(
            row=5, column=1, sticky=(tk.constants.E, tk.constants.W),
            padx=5, pady=10
        )

        self.tk_root.grid_columnconfigure(1, weight=1)
    
    def destroy(self):
        self.tk_root.destroy()

    def start_game(self):
        self.tk_root.withdraw()
        self.make_window()

    def make_window(self):
        self.find_difficulty(self.var)

        pygame.display.set_mode((500, 500))

        height = self.field_y
        width = self.field_x
        display_height = height * self.tile_size + self.tile_size
        display_width = width * self.tile_size

        display = pygame.display.set_mode((display_width, display_height))
        display.fill((0, 0, 0))

        pygame.display.set_caption("Minesweeper")

        pygame.init()

        Gameloop(display, self.field_x, self.field_y, self.mines, self.tile_size).start()

        pygame.display.quit()
        self.tk_root.deiconify()

    def find_difficulty(self, var):
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


if __name__ == "__main__":
    MainMenu()