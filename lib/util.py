import tkinter as tk
import tkinter.ttk as ttk
import io
import os
import pathlib
import json
from typing import *


Vars = Union[tk.BooleanVar, tk.StringVar, tk.IntVar, tk.DoubleVar]
studentsJson: dict = {}
groupsJson: dict = {}
reasonsJson: dict = {}
infoJson: dict = {}
scoresJson: dict = {}


def getJsonDada(
    name: Literal["student", "group", "reason", "score", "info", "all"]
) -> Union[Tuple[dict, dict, dict, dict, dict], dict]:
    global studentsJson, groupsJson, reasonsJson, scoresJson, infoJson
    if studentsJson and groupsJson and reasonsJson:
        if name == "student":
            return studentsJson
        elif name == "group":
            return groupsJson
        elif name == "reason":
            return reasonsJson
        elif name == "score":
            return scoresJson
        elif name == "info":
            return infoJson
        else:
            return studentsJson, groupsJson, reasonsJson, scoresJson, infoJson
    try:
        __studentsIO = open(
            pathlib.Path(os.getcwd()).joinpath("data").joinpath("students.json"),
            "r",
            encoding="utf-8",
        )
        studentsJson = json.loads(__studentsIO.read())
        __groupsIO = open(
            pathlib.Path(os.getcwd()).joinpath("data").joinpath("groups.json"),
            "r",
            encoding="utf-8",
        )
        groupsJson = json.loads(__groupsIO.read())
        __reasonsIO = open(
            pathlib.Path(os.getcwd()).joinpath("data").joinpath("reasons.json"),
            "r",
            encoding="utf-8",
        )
        reasonsJson = json.loads(__reasonsIO.read())
        __scoresIO = open(
            pathlib.Path(os.getcwd()).joinpath("data").joinpath("scores.json"),
            "r",
            encoding="utf-8",
        )
        scoresJson = json.loads(__scoresIO.read())
        __infoIO = open(
            pathlib.Path(os.getcwd()).joinpath("data").joinpath("info.json"),
            "r",
            encoding="utf-8",
        )
        infoJson = json.loads(__infoIO.read())
        __studentsIO.close()
        __groupsIO.close()
        __reasonsIO.close()
        __scoresIO.close()
        __infoIO.close()
    except json.decoder.JSONDecodeError:
        studentsJson = groupsJson = reasonsJson = scoresJson = infoJson = {}
    if name == "student":
        return studentsJson
    elif name == "group":
        return groupsJson
    elif name == "reason":
        return reasonsJson
    elif name == "score":
        return scoresJson
    elif name == "info":
        return infoJson
    else:
        return studentsJson, groupsJson, reasonsJson, scoresJson, infoJson


def getCallback(func: Callable, *args, **kwargs) -> Callable:
    """Return a Callback function for the given function with the given arguments."""
    return lambda: func(*args, **kwargs)


def createCheckButton(
    master: tk.Tk,
    text: str,
    var: Vars,
    func: Callable[[], None],
    onVar: Any = True,
    offVar: Any = False,
    *args,
    **kwargs
) -> ttk.Checkbutton:
    """Return a CheckButton with the given text and commands."""
    return ttk.Checkbutton(
        master,
        text=text,
        onvalue=onVar,
        command=func,
        offvalue=offVar,
        variable=var,
        *args,
        **kwargs
    )


def toFrame(
    master: tk.Tk,
    fromFrame: Union[tk.Tk, ttk.Frame, list],
    toFrameClass: Callable[[tk.Tk], None],
) -> None:
    """Destroy current frame and create a new frame"""
    if type(fromFrame) == list:
        for frame in fromFrame:
            frame.destroy()
    else:
        fromFrame.destroy()
    toFrameClass(master)


__all__ = [
    "getCallback",
    "createCheckButton",
    "toFrame",
    "Vars",
    "studentsJson",
    "groupsJson",
    "reasonsJson",
]
