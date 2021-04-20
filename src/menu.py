from tkinter import Tk, ttk, StringVar

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        start_button = ttk.Button(
            master=self._root,
            text="Pelaa",
            # command=
        )

        exit_button = ttk.Button(
            master=self._root,
            text="Poistu",
            # command=
        )

        start_button.pack()
        exit_button.pack()

window = Tk()
window.title("Minesweeper menu")

ui = UI(window)
ui.start()

window.mainloop()