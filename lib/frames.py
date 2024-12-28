import tkinter as tk
from tkinter import ttk, messagebox
from typing import *


class initWindow(tk.Tk):
    """Init window of the program"""

    def __init__(self) -> None:
        super().__init__()
        self.geometry("500x500")
        self.title("班级登分程序")


class mainFrame(object):
    """Main frame of the program"""

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        addButton = ttk.Button(self.frame, text="加分", command=self.add)
        addButton.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

        deleteButton = ttk.Button(self.frame, text="减分", command=self.delete)
        deleteButton.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

        writeButton = ttk.Button(self.frame, text="直接修改", command=self.write)
        writeButton.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

        searchButton = ttk.Button(self.frame, text="查询", command=self.search)
        searchButton.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

        rankButton = ttk.Button(self.frame, text="排行榜", command=self.rank)
        rankButton.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

    def add(self) -> None: ...
    def delete(self) -> None: ...
    def write(self) -> None: ...
    def search(self) -> None: ...
    def rank(self) -> None: ...


class add:
    def __init__(self, master):
        self.master = master
        self.win = Frame(self.master)
        self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

        label1 = Label(self.win, text="加分界面")
        label1.pack()

        label2 = Label(self.win, text="学号")
        label2.place(relx=0, rely=0.1)

        label3 = Label(self.win, text="加的分数")
        label3.place(relx=0.7, rely=0.1)

        label4 = Label(self.win, text="加分原因")
        label4.place(relx=0.7, rely=0.4)

        self.csb_dict["1"] = Checkbutton(
            self.win, text="1", command=lambda: self.set_value("1")
        )

        entry1 = Entry(self.win)
        entry1.place(relx=0.7, rely=0.2, relwidth=0.3)

        entry2 = Entry(self.win)
        entry2.place(relx=0.7, rely=0.5, relwidth=0.3)

        button1 = Button(self.win, text="返回", command=self.back)
        button1.place(relx=0, rely=0.9, relwidth=0.2)

        button2 = Button(
            self.win, text="确定", command=lambda: self.yes(entry1, entry2)
        )
        button2.place(relx=0.8, rely=0.9, relwidth=0.2)

    def back(self):
        self.win.destroy()
        main_window(self.master)

    def set_value(self, value):
        if self.csbv_dict[value] == 0:
            self.csbv_dict[value] = 1
        else:
            self.csbv_dict[value] = 0
        print(self.csbv_dict[value])

    def set_all(self):
        all_value = self.csbv_dict["all"]
        if all_value == 0:
            for num in self.csb_dict.keys():
                self.csb_dict[num].config(state=DISABLED)
            self.csb_dict["all"].config(state=NORMAL)
            self.csbv_dict["all"] = 1
        else:
            for num in self.csb_dict.keys():
                self.csb_dict[num].config(state=NORMAL)
            self.csbv_dict["all"] = 0

    def yes(self, entry1, entry2):
        global class_info
        get_num = int(entry1.get())
        get_info = entry2.get()
        if self.csbv_dict["all"] == 1:
            for nums in self.csbv_dict.keys():
                if nums != "all":
                    class_info[nums]["总分"] += get_num
                    class_info[nums]["加减分数"] += get_num
                    time = ti.localtime()
                    class_info[nums]["今日加减分数原因"].append(
                        f"{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒"
                        + get_info
                        + " +{}".format(str(get_num))
                    )
                else:
                    pass
        else:
            for nums in self.csbv_dict.keys():
                if nums != "all" and self.csbv_dict[nums] == 1:
                    class_info[nums]["总分"] += get_num
                    class_info[nums]["加减分数"] += get_num
                    time = ti.localtime()
                    class_info[nums]["今日加减分数原因"].append(
                        f"{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒"
                        + get_info
                        + " +{}".format(str(get_num))
                    )
                else:
                    pass
        user_name = getusername.getuser()
        with open(
            file=r"C:\Users\{}\.class\class_info.json".format(user_name),
            mode="w",
            encoding="utf-8",
        ) as f:
            f.write(str(class_info))
            f.close()
        showinfo(title="提示", message="加分成功！")
