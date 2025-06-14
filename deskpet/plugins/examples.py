from . import *
import tkinter as tk
import tkinter.messagebox as tkm


class ExitChoice(ChoiceBase):
    def __init__(self, main_window):
        super().__init__(main_window)

    def cmd(self):
        import sys

        sys.exit()

    def apply(self):
        button = ChoiceBuilder(
            menu_window=self.main_window,
            cmd=self.cmd,
            text="退出",
        ).apply()
        return button


class AboutChoice(ChoiceBase):
    def __init__(self, main_window):
        super().__init__(main_window)

    def cmd(self):
        dialog_box(
            "关于",
            """

信息:            
FexPet v0.0.1 内测版
项目地址: https://github.com/FexCode/DeskPet
作者: FexCode
严禁抄袭! 未授权,禁止传播
""",
        )

    def apply(self):
        button = ChoiceBuilder(
            menu_window=self.main_window,
            cmd=self.cmd,
            text="关于",
        ).apply()
        return button


class MenuExampleChoice(ChoiceBase):
    def __init__(self, main_window):
        super().__init__(main_window)

    def cmd(self):
        with SubMenu(self.main_window) as menu:
            menu.add_command(
                label="选项",
                command=lambda: tkm.showinfo("提示", "选项功能待实现"),
            )
            menu.add_command(
                label="选项2",
                command=lambda: tkm.showinfo("提示", "选项2功能待实现"),
            )
            menu.add_command(
                label="选项3",
                command=lambda: tkm.showinfo("提示", "选项3功能待实现"),
            )
            menu.add_separator()
            menu.add_command(label="取消", command=menu.destroy)

    def apply(self):
        button = ChoiceBuilder(
            menu_window=self.main_window,
            cmd=self.cmd,
            text="选项功能示例",
        ).apply()
        return button
