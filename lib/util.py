import tkinter as tk
import tkinter.ttk as ttk
import os
import pathlib
import json
import logging
from typing import *

dataPath: pathlib.Path = pathlib.Path(os.getcwd()).joinpath("data")


def initFolder() -> bool:
    isinitalized = True
    if dataPath.exists() == False:
        os.mkdir(dataPath)
        isinitalized = False
    if dataPath.joinpath("students.json").exists() == False:
        io = open(dataPath.joinpath("students.json"), "w", encoding='utf-8')
        io.write("{}")
        io.close()
        isinitalized = False
    if dataPath.joinpath("groups.json").exists() == False:
        io = open(dataPath.joinpath("groups.json"), "w", encoding='utf-8')
        io.write("{}")
        io.close()
    if dataPath.joinpath("reasons.json").exists() == False:
        io = open(dataPath.joinpath("reasons.json"), "w", encoding='utf-8')
        io.write("{}")
        io.close()
    if dataPath.joinpath("scores.json").exists() == False:
        io = open(dataPath.joinpath("scores.json"), "w", encoding='utf-8')
        io.write("{}")
        io.close()
    if dataPath.joinpath("info.json").exists() == False:
        io = open(dataPath.joinpath("info.json"), "w", encoding='utf-8')
        io.write("{\"data\": []}")
        io.close()
    return isinitalized


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s %(levelname)s]%(name)s $ %(message)s",
)
formatter = logging.Formatter("[%(asctime)s]%(name)s %(levelname)s %(message)s")
rootLogger = logging.getLogger("root")
fileHandler = logging.FileHandler(pathlib.Path(os.getcwd()).joinpath("log.log"), encoding="utf-8")
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.INFO)
rootLogger.setLevel(logging.INFO)
rootLogger.addHandler(fileHandler)

rootLogger.info("Logger initialized.")

Vars = Union[tk.BooleanVar, tk.StringVar, tk.IntVar, tk.DoubleVar]


class Json(object):
    """A class to handle the json data."""

    def __init__(self, path: Union[str, pathlib.Path], encoding: str = "utf-8") -> None:
        self.path = path
        self.encoding = encoding
        self.data: dict = {}
        self.logger = rootLogger.getChild(f"json-{self.path}")
        self.read()

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        del self.data[key]

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator:
        return iter(self.data)

    def read(self) -> None:
        try:
            self.logger.info("Reading json file.")
            self.io = open(self.path, "r", encoding=self.encoding)
            self.data = json.loads(self.io.read())
            self.io.close()
        except (FileNotFoundError, FileExistsError):
            self.logger.error("Error reading json file.")
        except json.JSONDecodeError:
            self.logger.error("Error decoding json file.")
        finally:
            self.logger.info("Json file read.")

    def write(self) -> None:
        self.logger.info("Writing json file.")
        self.io = open(self.path, "w", encoding=self.encoding)
        self.io.write(str(json.dumps(self.data, indent=4, ensure_ascii=False)))
        self.io.close()
        self.logger.info("Json file wrote.")

    def get(self) -> dict:
        return self.data


jsons: Dict[str, Json] = {
    "students": Json(dataPath.joinpath("students.json")),
    "groups": Json(dataPath.joinpath("groups.json")),
    "reasons": Json(dataPath.joinpath("reasons.json")),
    "scores": Json(dataPath.joinpath("scores.json")),
    "info": Json(dataPath.joinpath("info.json")),
}


def getJsonData(
    name: Literal["students", "groups", "reasons", "scores", "info", "all"]
) -> Union[Dict[str, Json], Json]:
    if name == "all":
        return jsons
    else:
        return jsons[name]


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
    fromFrame: tk.Widget,
    toFrameClass: Callable[[tk.Tk], None],
) -> None:
    """Destroy current frame and create a new frame"""
    if type(fromFrame) == list:
        for frame in fromFrame:
            frame.destroy()
    else:
        fromFrame.destroy()
    toFrameClass(master)


__all__ = ["createCheckButton", "toFrame", "Vars", "Json", "getJsonData", "jsons"]
