from abc import ABC, abstractmethod
import tkinter as tk
from typing import TypeVar


class ChoiceBase(ABC):
    def __init__(self, main_window):
        self.main_window = main_window

    @abstractmethod
    def cmd(self):
        pass

    @abstractmethod
    def apply(self) -> tk.Button:
        pass
