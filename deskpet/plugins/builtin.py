import tkinter as tk
import tkinter.messagebox as tkm


class ChoiceBuilder:
    def __init__(
        self,
        menu_window,
        cmd,
        text,
        bg="#f0f0f0",
        fg="black",
        font=("Arial", 10),
        borderwidth=1,
    ):
        self.menu_window = menu_window
        self.cmd = cmd
        self.text = text
        self.bg = bg
        self.fg = fg
        self.font = font
        self.borderwidth = borderwidth

    def apply(self):
        button = tk.Button(
            self.menu_window,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            borderwidth=self.borderwidth,
            command=self.cmd,
        )
        button.pack(fill="x", pady=5, padx=10)
        return button


def dialog_box(title, message):
    tkm.showinfo(title, message)

class SubMenu:
    def __init__(self, main_window):
        self.main_window = main_window
        self.menu = tk.Menu(self.main_window, tearoff=0)

    def __enter__(self):
        return self.menu

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.menu.tk_popup(
                self.main_window.winfo_pointerx(), self.main_window.winfo_pointery()
            )
        finally:
            self.menu.grab_release()
