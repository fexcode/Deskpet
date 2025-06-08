from . import *
import tkinter.messagebox as tkm


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
        dialog_box(
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
