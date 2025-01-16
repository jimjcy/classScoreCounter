import tkinter as tk
import tkinter.ttk as ttk
import os
import pathlib
import json
import logging
from typing import *

dataPath: pathlib.Path = pathlib.Path(os.getcwd()).joinpath("data")


def createFile(file: Union[str, pathlib.Path]) -> None:
    if pathlib.Path(file).exists() == False:
        open(file, "w", encoding="utf-8").close()


def initFolder() -> None:
    if dataPath.exists() == False:
        os.mkdir(dataPath)
    if dataPath.joinpath("students.json").exists() == False:
        createFile(dataPath.joinpath("students.json"))
    if dataPath.joinpath("groups.json").exists() == False:
        createFile(dataPath.joinpath("groups.json"))
    if dataPath.joinpath("reasons.json").exists() == False:
        createFile(dataPath.joinpath("reasons.json"))
    if dataPath.joinpath("scores.json").exists() == False:
        createFile(dataPath.joinpath("scores.json"))
    if dataPath.joinpath("info.json").exists() == False:
        createFile(dataPath.joinpath("info.json"))


initFolder()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s %(levelname)s]%(name)s $ %(message)s",
)
formatter = logging.Formatter("[%(asctime)s]%(name)s %(levelname)s %(message)s")
rootLoggger = logging.getLogger("root")
fileHandler = logging.FileHandler(
    dataPath.joinpath("log.log"), encoding="utf-8"
)
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.INFO)
rootLoggger.setLevel(logging.INFO)
rootLoggger.addHandler(fileHandler)

rootLoggger.info("Logger initialized.")
rootLoggger.info("File created.")

Vars = Union[tk.BooleanVar, tk.StringVar, tk.IntVar, tk.DoubleVar]
jsonData: Dict[str, Union[dict, Dict[str, Union[str, int, List[str]]]]] = {
    "students": {},
    "groups": {},
    "reasons": {},
    "scores": {},
    "info": {},
}


def __readJsonData() -> None:
    global jsonData, rootLoggger
    rootLoggger.info("Reading JSON data.")
    try:
        for i in jsonData:
            __io = open(
                pathlib.Path(os.getcwd()).joinpath("data").joinpath(f"{i}.json"),
                "r",
                encoding="utf-8",
            )
            jsonData[i] = json.loads(__io.read())
            __io.close()
        rootLoggger.info("JSON data read.")
    except json.decoder.JSONDecodeError:
        jsonData = {
            "students": {},
            "groups": {},
            "reasons": {},
            "scores": {},
            "info": {},
        }
        rootLoggger.error("JSON data read failed.")


def getJsonData(
    name: Literal["students", "groups", "reasons", "scores", "info", "all"]
) -> Union[Dict[str, Union[dict, Dict[str, Union[str, int, List[str]]]]], dict]:
    __readJsonData()
    if name == "all":
        return jsonData
    else:
        return jsonData[name]


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
    "jsonData"
]
