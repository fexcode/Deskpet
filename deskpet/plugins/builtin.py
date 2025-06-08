import tkinter as tk
import tkinter.messagebox as tkm
from .base import ChoiceBase


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
