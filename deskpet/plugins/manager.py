from typing import List, Type
import tkinter as tk
from .base import ChoiceBase


class ChoiceManager:
    def __init__(self):
        self._all_choices = []

    def add_choice(self, choice_class: Type[ChoiceBase]):
        self.all_choices.append(choice_class)
        return self

    def build_choices(self, main_window: tk.Tk) -> List[tk.Button]:
        """Build all available choices in the menu window"""
        choices: List[tk.Button] = []
        for choice_class in self.all_choices:
            choice = choice_class(main_window)
            choices.append(choice.apply())
        return choices

    @property
    def all_choices(self) -> List[Type[ChoiceBase]]:
        return self._all_choices


def build_choices(main_window: tk.Tk, choice_manager: ChoiceManager) -> List[tk.Button]:
    """Build all available choices in the menu window"""
    choices: List[tk.Button] = []
    for choice_class in choice_manager.all_choices:
        choice = choice_class(main_window)
        choices.append(choice.apply())
    return choices
