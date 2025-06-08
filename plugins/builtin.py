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


class ExitChoice(ChoiceBase):
    def __init__(self, main_window):
        super().__init__(main_window)

    def cmd(self):
        import sys

        sys.exit()

    def apply(self):
        button = ChoiceBuilder(
            self.main_window,
            self.cmd,
            "退出",
        ).apply()
        return button


class TutorialChoice(ChoiceBase):
    def __init__(self, main_window):
        super().__init__(main_window)

    def cmd(self):
        tkm.showinfo(
            "教程",
            """

信息:            
FexPet 0.0.0 内测版
作者: FexCode
严禁抄袭! 未授权,禁止传播
""",
        )

    def apply(self):
        button = ChoiceBuilder(
            self.main_window,
            self.cmd,
            "教程",
        ).apply()
        return button
