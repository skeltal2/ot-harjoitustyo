import tkinter as tk
import sqlite3
from tkinter import ttk

class HighScores:
    """Create window to display high scores

    Attributes:
        database: Database where scores and names are stored
        tk_root: Tkinter window root
        menu: MainMenu object to display when this window is destroyed
    """
    def __init__(self, menu):
        """Initialize high score window

        Args:
            menu: MainMenu object to display when this window is destroyed
        """
        self.database = sqlite3.connect("src/database/scores.db")
        self.tk_root = tk.Tk()
        self.menu = menu

        # Center window
        screen_x = (self.tk_root.winfo_screenwidth()/2) - (540/2)
        screen_y = (self.tk_root.winfo_screenheight()/2) - (800/2)
        self.tk_root.geometry(f"540x800+{int(screen_x)}+{int(screen_y)}")

        self._load_data()
        # Create a table for each game difficulty
        self._create_table(self.scores_1, 1)
        self._create_table(self.scores_2, 2)
        self._create_table(self.scores_3, 3)

        self.tk_root.title("Tulokset")

        # Button returns back to main menu and destroys this window
        button = tk.Button(
            self.tk_root,
            text="Takaisin",
            padx=20,
            command=self._return_to_main_menu
        )

        button.pack(pady=10)

        self.tk_root.protocol("WM_DELETE_WINDOW", self._destroy)
        self.tk_root.mainloop()

    def _load_data(self):
        # Create table if it doesn't exist
        self.database.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY,
                score INTEGER,
                mode INTEGER,
                name TEXT
            );
            """)
        self.database.commit()

        self.scores_1 = self.database.execute(
            "SELECT score, name FROM scores WHERE mode = 1 ORDER BY score;"
        ).fetchall()
        self.scores_2 = self.database.execute(
            "SELECT score, name FROM scores WHERE mode = 2 ORDER BY score;"
        ).fetchall()
        self.scores_3 = self.database.execute(
            "SELECT score, name FROM scores WHERE mode = 3 ORDER BY score;"
        ).fetchall()


    def _create_table(self, data, mode):
        # Set title for table
        if mode == 1:
            text = "Helppo"
        elif mode == 2:
            text = "Keskitaso"
        elif mode == 3:
            text = "Vaikea"

        # Create table
        label = tk.Label(self.tk_root, text=text)
        tree = ttk.Treeview(self.tk_root, columns=("Score", "Name"), show="headings")
        tree.heading("Score", text="Aika")
        tree.heading("Name", text="Nimi")

        # Insert data to table
        for i in data:
            seconds = "0" + str(int((i[0]/1000)%60))
            minutes = "0" + str(int((i[0]/(1000*60))%60))

            time = f"{minutes[-2:]}:{seconds[-2:]}"

            tree.insert("", "end", values=(time, i[1]))

        label.pack()
        tree.pack()

    def _return_to_main_menu(self):
        self.menu.deiconify()
        self.tk_root.destroy()

    def _destroy(self):
        self.menu.destroy()
        self.tk_root.destroy()
