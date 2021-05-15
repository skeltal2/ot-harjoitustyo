import tkinter as tk
import sqlite3
from tkinter import ttk

class HighScores:
    def __init__(self, menu):
        self.db = sqlite3.connect("src/database/scores.db")
        self.tk_root = tk.Tk()
        self.menu = menu

        screen_x = (self.tk_root.winfo_screenwidth()/2) - (540/2)
        screen_y = (self.tk_root.winfo_screenheight()/2) - (800/2)
        self.tk_root.geometry(f"540x800+{int(screen_x)}+{int(screen_y)}")

        self._load_data()
        self._create_table(self.scores_1, 1)
        self._create_table(self.scores_2, 2)
        self._create_table(self.scores_3, 3)

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
        self.scores_1 = self.db.execute("SELECT score, name FROM scores WHERE mode = 1 ORDER BY score;").fetchall()
        self.scores_2 = self.db.execute("SELECT score, name FROM scores WHERE mode = 2 ORDER BY score;").fetchall()
        self.scores_3 = self.db.execute("SELECT score, name FROM scores WHERE mode = 3 ORDER BY score;").fetchall()

    def _create_table(self, data, mode):
        if mode == 1:
            text = "Helppo"
        elif mode == 2:
            text = "Keskitaso"
        elif mode == 3:
            text = "Vaikea"

        label = tk.Label(self.tk_root, text=text)
        tree = ttk.Treeview(self.tk_root, columns=("Score", "Name"), show="headings")
        tree.heading("Score", text="Aika")
        tree.heading("Name", text="Nimi")
        
        for i in data:
            sec = "0" + str(int((i[0]/1000)%60))
            min = "0" + str(int((i[0]/(1000*60))%60))

            time = f"{min[-2:]}:{sec[-2:]}"

            tree.insert("", "end", values=(time, i[1]))
        
        label.pack()
        tree.pack()
    
    def _return_to_main_menu(self):
        self.menu.deiconify()
        self.tk_root.destroy()
    
    def _destroy(self):
        self.menu.destroy()
        self.tk_root.destroy()

if __name__ == "__main__":
    HighScores()
