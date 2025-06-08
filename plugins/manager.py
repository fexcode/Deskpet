from typing import List, Type
import tkinter as tk
from .builtin import ExitChoice, TutorialChoice
from .base import ChoiceBase

ALL_CHOICES: List[Type[ChoiceBase]] = [
    TutorialChoice,
    ExitChoice,
]


def build_choices(main_window: tk.Tk) -> List[tk.Button]:
    """Build all available choices in the menu window"""
    choices: List[tk.Button] = []
    for choice_class in ALL_CHOICES:
        choice = choice_class(main_window)
        choices.append(choice.apply())
    return choices
