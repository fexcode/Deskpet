import tkinter as tk
from ..plugins.manager import build_choices
from .pet import Pet
from deskpet.utils import logger


class App:
    def __init__(self, pet=None):
        self.pet = pet if pet is not None else Pet()
        self._setup_menu()
        self._bind_events()

    def _setup_menu(self):
        """创建菜单窗口"""
        root = self.pet.get_root()
        posX, posY = self.pet.posX, self.pet.posY

        self.menu_window = tk.Toplevel(root)
        self.menu_window.overrideredirect(True)  # 去掉边框
        self.menu_window.configure(bg="#f0f0f0")  # 设置背景颜色为淡灰色
        self.menu_window.geometry(f"150x200+{posX - 150}+{posY}")  # 菜单显示在桌宠左侧
        self.menu_window.attributes("-topmost", 1)  # 置顶
        self.menu_window.withdraw()  # 初始时隐藏菜单窗口
        logger.info(f"init: posX: {posX}, posY: {posY}")

        # 添加菜单标题栏
        title_bar = tk.Frame(self.menu_window, bg="#333333", height=30)
        title_bar.pack(fill="x")

        title_label = tk.Label(
            title_bar, text="菜单", bg="#333333", fg="white", font=("Arial", 12, "bold")
        )
        title_label.pack(side="left", padx=10)

        # 添加关闭按钮
        close_button = tk.Button(
            title_bar,
            text="X",
            bg="#333333",
            fg="white",
            font=("Arial", 12, "bold"),
            borderwidth=0,
            command=self._close_menu,
        )
        close_button.pack(side="right", padx=10)

        self.pet.build_choices(self.menu_window)

        logger.info("init: menu window created")

    def _close_menu(self):
        """关闭菜单"""
        self.menu_window.withdraw()
        logger.info("close: menu window closed")
        logger.info(f"in func _close_menu: posX: {self.pet.posX}, posY: {self.pet.posY}")

    def _show_menu(self, event=None):
        """显示/隐藏菜单"""
        posX, posY = self.pet.posX, self.pet.posY
        logger.info(f"in func _show_menu: {self.pet.posX=}, {self.pet.posY}")
        self.menu_window.geometry(f"150x200+{posX-150}+{posY}")  # 菜单显示在桌宠左侧
        if self.menu_window.winfo_ismapped():
            self.menu_window.withdraw()
        else:
            self.menu_window.deiconify()


    def _bind_events(self):
        """绑定事件"""
        self.pet.bind_double_click(self._show_menu)

    def run(self):
        """运行应用主循环"""
        self.pet.get_root().mainloop()
