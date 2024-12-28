import tkinter as tk
import tkinter.ttk as ttk
from typing import *


def getCallback(func: Callable, *args, **kwargs) -> Callable:
    """Return a Callback function for the given function with the given arguments."""
    return lambda: func(*args, **kwargs)


def summonCheckButton(master: tk.Tk, text: str, func: Callable, *args, **kwargs) -> ttk.Checkbutton:
    """Return a CheckButton with the given text and commands."""
    return ttk.Checkbutton(master, text=text, command=func, *args, **kwargs)
