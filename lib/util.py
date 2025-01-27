import tkinter as tk
import tkinter.ttk as ttk
import os
from typing import *

try:
    import datas
except ModuleNotFoundError:
    from . import datas

rootLogger = datas.rootLogger


def initFolder() -> bool:
    isinitalized = True
    if datas.dataPath.exists() == False:
        os.mkdir(datas.dataPath)
        isinitalized = False
    if datas.dataPath.joinpath("students.json").exists() == False:
        io = open(datas.dataPath.joinpath("students.json"), "w", encoding="utf-8")
        io.write("{}")
        io.close()
        isinitalized = False
    if datas.dataPath.joinpath("groups.json").exists() == False:
        io = open(datas.dataPath.joinpath("groups.json"), "w", encoding="utf-8")
        io.write("{}")
        io.close()
    if datas.dataPath.joinpath("reasons.json").exists() == False:
        io = open(datas.dataPath.joinpath("reasons.json"), "w", encoding="utf-8")
        io.write("{}")
        io.close()
    if datas.dataPath.joinpath("scores.json").exists() == False:
        io = open(datas.dataPath.joinpath("scores.json"), "w", encoding="utf-8")
        io.write("{}")
        io.close()
    if datas.dataPath.joinpath("info.json").exists() == False:
        io = open(datas.dataPath.joinpath("info.json"), "w", encoding="utf-8")
        io.write('{"data": []}')
        io.close()
    return isinitalized


def getJsonData(
    name: Literal["students", "groups", "reasons", "scores", "info", "all"]
) -> Union[Dict[str, datas.Json], datas.Json]:
    if name == "all":
        return datas.jsons
    else:
        return datas.jsons[name]


def createCheckButton(
    master: tk.Tk,
    text: str,
    var: datas.Vars,
    func: Callable[[], None],
    onVar: Any = True,
    offVar: Any = False,
    *args,
    **kwargs,
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
        **kwargs,
    )


def toFrame(
    master: tk.Tk,
    fromFrame: Union[tk.Widget, List[tk.Widget]],
    toFrameClass: Callable[[tk.Tk], None],
) -> None:
    """Destroy current frame and create a new frame"""
    if type(fromFrame) == list:
        for frame in fromFrame:
            frame.destroy()
    else:
        fromFrame.destroy()
    toFrameClass(master)


__all__ = ["createCheckButton", "toFrame", "getJsonData"]
