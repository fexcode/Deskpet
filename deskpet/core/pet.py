import tkinter as tk
from PIL import Image, ImageTk
import pyautogui as pt
from ..plugins.base import ChoiceBase
from ..plugins.manager import ChoiceManager
from typing import List, Type
from deskpet.utils import logger


class Pet:
    def __init__(
        self, image_path="./logo.png", choice_manager: ChoiceManager | None = None
    ):
        if choice_manager is None:
            self.choice_list = []
        else:
            self.choice_list = choice_manager.all_choices

        # 获取屏幕分辨率
        WIDTH, HEIGHT = pt.size()
        # 设置宠物图片的宽度和高度
        self.imgWidth, self.imgHeight = 200, 200
        # 设置宠物的初始位置（屏幕右下角）
        self.posX, self.posY = (
            WIDTH - self.imgWidth,
            HEIGHT - self.imgHeight - 40,
        )  # 减去任务栏高度

        # 创建主窗口
        self.root = tk.Tk()
        self.root.geometry(f"{self.imgWidth}x{self.imgHeight}+{self.posX}+{self.posY}")
        self.root.overrideredirect(True)  # 去掉窗口边框
        self.root.configure(bg="pink")
        self.root.attributes("-transparentcolor", "pink")  # 设置透明颜色为粉色
        self.root.wm_attributes("-topmost", 1)  # 窗口置顶

        # 加载并缩放图片
        original_image = Image.open(image_path)
        resized_image = original_image.resize((self.imgWidth, self.imgHeight))
        self.pet_photo = ImageTk.PhotoImage(resized_image)

        # 创建标签显示图片
        self.pet_label = tk.Label(self.root, image=self.pet_photo, bg="pink")
        self.pet_label.pack()

        # 绑定鼠标事件
        self.root.bind("<Button-1>", self._get_point)
        self.root.bind("<B1-Motion>", self._move_window)
        self.root.bind("<ButtonRelease-1>", self._stop_move)

    def _stop_move(self, event):
        logger.info(f"in _stop_move: {self.posX=}, {self.posY=}")

    def _get_point(self, event):
        self.posX, self.posY = self.root.winfo_x(), self.root.winfo_y()
        # self.root.winfo_x():  获取窗口左上角x坐标

    def _move_window(self, event):
        new_x = event.x_root - self.imgWidth // 2
        new_y = event.y_root - self.imgHeight // 2
        self.root.geometry(f"+{new_x}+{new_y}")
        # logger.info(f"in _move_window: {new_x=}, {new_y=},{self.posX=}, {self.posY=}")
        self.posX, self.posY = new_x, new_y

    def bind_double_click(self, callback):
        """绑定双击事件"""
        self.root.bind("<Double-Button-1>", callback)

    def get_root(self):
        """获取主窗口对象"""
        return self.root

    def build_choices(self, main_menu):
        for choice_class in self.choice_list:
            c = choice_class(main_menu)
            c.apply()
