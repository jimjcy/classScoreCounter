import tkinter as tk
from tkinter import ttk, messagebox
from typing import *
import functools
import pathlib
import os
import json
import time

try:
    import util
except ModuleNotFoundError:
    from . import util

rootLogger = util.rootLogger


class initWindow(tk.Tk):
    """Init window of the program"""

    def __init__(self) -> None:
        super().__init__()
        self.geometry("500x500")
        self.title("班级管理工具")


class createFileWindow(tk.Tk):
    """Create file window of the program"""

    def __init__(self) -> None:
        super().__init__()
        self.geometry("200x150")
        self.title("创建所需文件")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)

        ttk.Label(self, text="检测到您第一次启动本程序").pack()
        ttk.Label(self, text="需创建所需文件").pack()
        ttk.Label(self, text="请输入学生人数").pack()

        self.entry = ttk.Entry(self)
        self.entry.pack()

        self.button = ttk.Button(self, text="创建", command=self.createFile)
        self.button.pack()

    def createFile(self):
        try:
            studentCount = int(self.entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入一个整数")
            return
        if studentCount <= 0:
            messagebox.showerror("错误", "请输入一个大于0的整数")
            return
        for i in range(1, studentCount + 1):
            util.getJsonData("students")[str(i)] = ""
            util.getJsonData("scores")[str(i)] = 0
        util.getJsonData("students").write()
        util.getJsonData("scores").write()
        allJson = util.getJsonData("all")
        for i in allJson:
            allJson[i].read()
        self.destroy()

    def close(self):
        messagebox.showinfo("提示", "请根据指引完成程序设置")


class mainFrame(object):
    """Main frame of the program"""

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.aboutLabel = ttk.Label(self.frame, text="班级管理工具")
        self.aboutLabel.pack()

        self.addButton = ttk.Button(
            self.frame,
            text="分数管理",
            command=lambda: util.toFrame(self.master, self.frame, ScoreFrame),
        )
        self.addButton.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.1)

        self.searchButton = ttk.Button(
            self.frame,
            text="查询",
            command=lambda: util.toFrame(self.master, self.frame, searchFrame),
        )
        self.searchButton.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.1)

        self.rankButton = ttk.Button(
            self.frame,
            text="排行榜",
            command=lambda: util.toFrame(self.master, self.frame, rankFrame),
        )
        self.rankButton.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.1)

        self.splitLabel = ttk.Label(
            self.frame,
            text="========================实用小工具========================",
        )
        self.splitLabel.place(relx=0, rely=0.4, relwidth=1, relheight=0.1)

        self.randomStudentButton = ttk.Button(
            self.frame,
            text="随机点名",
            command=lambda: util.toFrame(self.master, self.frame, randomStudentFrame),
        )
        self.randomStudentButton.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.1)

        self.timerButton = ttk.Button(
            self.frame,
            text="倒计时",
            command=lambda: util.toFrame(self.master, self.frame, timerFrame),
        )
        self.timerButton.place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.1)

        self.aboutButton = ttk.Button(
            self.frame,
            text="关于",
            command=lambda: util.toFrame(self.master, self.frame, aboutFrame),
        )
        self.aboutButton.place(relx=0, rely=0.9, relwidth=0.2, relheight=0.1)

        self.exitButton = ttk.Button(
            self.frame,
            text="退出",
            command=lambda: self.master.destroy(),
        )
        self.exitButton.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)
        rootLogger.info("Main frame initialized.")


class ScoreFrame(object):
    def __init__(self, master: tk.Tk) -> None:
        self.logger = util.rootLogger.getChild("score")
        self.checkbuttonNumberDict: Dict[str, ttk.Checkbutton] = {}
        self.checkbuttonNumberStatus: Dict[str, tk.BooleanVar] = {
            "all": tk.BooleanVar()
        }
        self.checkbuttonNameDict: Dict[str, ttk.Checkbutton] = {}
        self.checkbuttonNameStatus: Dict[str, tk.BooleanVar] = {"all": tk.BooleanVar()}
        self.scoreSymbol = tk.StringVar()
        self.scoreValue = tk.IntVar()
        self.reasonMode = tk.StringVar()
        self.reasonText = tk.StringVar()
        self.scoreMode = tk.StringVar()
        self.master = master

        self.frameName = ttk.Label(self.master, text="管理分数界面")
        self.frameName.place(relx=0.4, rely=0, relheight=0.1)

        self.studentNotebook = ttk.Notebook(self.master)
        self.studentNotebook.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.studentNumberFrame = ttk.Frame(self.master)
        self.studentNameFrame = ttk.Frame(self.master)

        self.studentNotebook.add(self.studentNameFrame, text="姓名面板")
        self.studentNotebook.add(self.studentNumberFrame, text="学号面板")

        self.scoreFrame = ttk.Frame(self.master)
        self.scoreFrame.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)

        for i in range(1, len(util.getJsonData("students")) // 10 + 2):
            for j in range(1, 11):
                if (i - 1) * 10 + j > len(util.getJsonData("students")):
                    break
                boolvar = tk.BooleanVar()
                boolvar.set(False)
                checkButton = util.createCheckButton(
                    self.studentNumberFrame,
                    str((i - 1) * 10 + j),
                    boolvar,
                    functools.partial(self.setValue, "number", (i - 1) * 10 + j),
                )
                checkButton.place(
                    relx=(i - 1) / 10 + 0.05 * (i - 1), rely=j / 10 - 0.03 * (j - 1)
                )
                self.checkbuttonNumberStatus[str((i - 1) * 10 + j)] = boolvar
                self.checkbuttonNumberDict[str((i - 1) * 10 + j)] = checkButton

        self.checkbuttonNumberDict["all"] = util.createCheckButton(
            self.studentNumberFrame,
            "全选",
            self.checkbuttonNumberStatus["all"],
            lambda: self.setAll("number"),
        )
        self.checkbuttonNumberDict["all"].place(relx=0.8, rely=0.9)
        self.checkbuttonNumberStatus["all"].set(False)

        for i in range(
            1, len(util.getJsonData("students")) // 15 + 2
        ):  # 列的数量，每列x + 1（整除+1）+ 1（左闭右开）
            for j in range(1, 16):  # 行的数量，每行y + 1（左闭右开）
                if (i - 1) * 15 + j > len(util.getJsonData("students")):
                    break
                boolvar = tk.BooleanVar()
                boolvar.set(False)
                checkButton = util.createCheckButton(
                    self.studentNameFrame,
                    util.getJsonData("students")[str((i - 1) * 15 + j)],
                    boolvar,
                    functools.partial(self.setValue, "name", (i - 1) * 15 + j),
                )
                checkButton.place(
                    relx=(i - 1) / 10 + 0.1 * (i - 1), rely=j / 10 - 0.04 * (j - 1)
                )
                self.checkbuttonNameStatus[str((i - 1) * 15 + j)] = boolvar
                self.checkbuttonNameDict[str((i - 1) * 15 + j)] = checkButton

        self.checkbuttonNameDict["all"] = util.createCheckButton(
            self.studentNameFrame,
            "全选",
            self.checkbuttonNameStatus["all"],
            lambda: self.setAll("name"),
        )
        self.checkbuttonNameDict["all"].place(relx=0.8, rely=0.9)
        self.checkbuttonNameStatus["all"].set(False)

        # -----------------------------------------------------------------------------

        self.scoreLabel = ttk.Label(self.scoreFrame, text="分数面板")
        self.scoreLabel.place(relx=0, rely=0.1)

        self.scoreRadiobutton1 = ttk.Radiobutton(
            self.scoreFrame,
            text="加/减分",
            variable=self.scoreMode,
            value="addorsub",
            command=self.setScoreMode,
        )
        self.scoreRadiobutton1.place(relx=0, rely=0.2)

        self.scoreSymbolCombobox = ttk.Combobox(
            self.scoreFrame, textvariable=self.scoreSymbol
        )
        self.scoreSymbolCombobox["values"] = ["+", "-"]
        self.scoreSymbolCombobox.place(relx=0.3, rely=0.2, relwidth=0.3)
        self.scoreSymbolCombobox.current(0)

        self.scoreValueCombobox = ttk.Combobox(
            self.scoreFrame, textvariable=self.scoreValue
        )
        self.scoreValueCombobox["values"] = [x for x in range(1, 11)]
        self.scoreValueCombobox.place(relx=0.6, rely=0.2, relwidth=0.4)
        self.scoreValueCombobox.current(0)

        self.scoreRadiobutton2 = ttk.Radiobutton(
            self.scoreFrame,
            text="直接修改",
            variable=self.scoreMode,
            value="input",
            command=self.setScoreMode,
        )
        self.scoreRadiobutton2.place(relx=0, rely=0.3)

        self.scoreEntry = ttk.Entry(self.scoreFrame, textvariable=self.scoreValue)
        self.scoreEntry.place(relx=0.35, rely=0.3, relwidth=0.65)
        self.scoreEntry.config(state="disabled")

        self.scoreMode.set("addorsub")

        # -----------------------------------------------------------------------------

        self.reasonLabel = ttk.Label(self.scoreFrame, text="加分原因")
        self.reasonLabel.place(relx=0, rely=0.4)

        self.reasonRadiobutton1 = ttk.Radiobutton(
            self.scoreFrame,
            text="选择预设原因",
            variable=self.reasonMode,
            value="json",
            command=self.setReasonMode,
        )
        self.reasonRadiobutton1.place(relx=0, rely=0.5)

        self.reasonCombobox = ttk.Combobox(
            self.scoreFrame, textvariable=self.reasonText
        )
        self.reasonCombobox["values"] = util.getJsonData("reasons")["data"]
        self.reasonCombobox.place(relx=0.5, rely=0.5, relwidth=0.5)
        self.reasonCombobox.current(0)

        self.reasonRadiobutton2 = ttk.Radiobutton(
            self.scoreFrame,
            text="自定义原因",
            variable=self.reasonMode,
            value="input",
            command=self.setReasonMode,
        )
        self.reasonRadiobutton2.place(relx=0, rely=0.6)

        self.reasonEntry = ttk.Entry(self.scoreFrame, textvariable=self.reasonText)
        self.reasonEntry.place(relx=0.45, rely=0.6, relwidth=0.55)
        self.reasonEntry.config(state="disabled")

        self.reasonRadiobutton3 = ttk.Radiobutton(
            self.scoreFrame,
            text="无",
            variable=self.reasonMode,
            value="none",
            command=self.setReasonMode,
        )
        self.reasonRadiobutton3.place(relx=0, rely=0.7)

        self.reasonMode.set("json")

        self.backButton = ttk.Button(
            self.scoreFrame,
            text="返回",
            command=lambda: util.toFrame(
                self.master,
                [self.studentNotebook, self.scoreFrame, self.frameName],
                mainFrame,
            ),
        )
        self.backButton.place(relx=0, rely=0.9, relheight=0.1)

        self.yesButton = ttk.Button(self.scoreFrame, text="确定", command=self.ok)
        self.yesButton.place(relx=0.6, rely=0.9, relheight=0.1)

        rootLogger.info("Score frame initialized.")

    def setValue(
        self,
        fromFrame: Literal["number", "name"],
        index: Union[str, int],
        toIndex: Union[str, int, None] = None,
    ) -> None:
        if toIndex is None:
            toIndex = index
        if (self.checkbuttonNameStatus["all"].get() or self.checkbuttonNumberStatus["all"].get()) and toIndex != "all":
            self.checkbuttonNameStatus["all"].set(False)
            self.checkbuttonNumberStatus["all"].set(False)
        if fromFrame == "number":
            self.checkbuttonNumberStatus[str(index)].set(
                self.checkbuttonNumberStatus[str(toIndex)].get()
            )
            self.checkbuttonNameStatus[str(index)].set(
                self.checkbuttonNumberStatus[str(toIndex)].get()
            )
        elif fromFrame == "name":
            self.checkbuttonNameStatus[str(index)].set(
                self.checkbuttonNameStatus[str(toIndex)].get()
            )
            self.checkbuttonNumberStatus[str(index)].set(
                self.checkbuttonNameStatus[str(toIndex)].get()
            )
        if toIndex != "all":
            self.logger.info(
                "Set " + str(index) + " to " + str(self.checkbuttonNumberStatus[str(index)].get())
            )

    def setAll(self, fromFrame: Literal["number", "name"]) -> None:
        for i in range(1, len(self.checkbuttonNumberDict)):
            self.setValue(fromFrame, str(i), "all")
        self.setValue(fromFrame, "all", "all")
        self.logger.info(f"Set all students to {str(self.checkbuttonNumberStatus['all'].get())}")

    def setReasonMode(self) -> None:
        if self.reasonMode.get() == "json":
            self.reasonCombobox.current(0)
            self.reasonCombobox.config(state="normal")
            self.reasonEntry.config(state="disabled")
        elif self.reasonMode.get() == "input":
            self.reasonText.set("")
            self.reasonEntry.config(state="normal")
            self.reasonCombobox.config(state="disabled")
        else:
            self.reasonCombobox.config(state="disabled")
            self.reasonEntry.config(state="disabled")
            self.reasonText.set("无")
        self.logger.info("reason mode changed to " + self.reasonMode.get())
        

    def setScoreMode(self) -> None:
        if self.scoreMode.get() == "addorsub":
            self.scoreSymbolCombobox.current(0)
            self.scoreValueCombobox.current(0)
            self.scoreSymbolCombobox.config(state="normal")
            self.scoreValueCombobox.config(state="normal")
            self.scoreEntry.config(state="disabled")
        else:
            self.scoreSymbolCombobox.config(state="disabled")
            self.scoreValueCombobox.config(state="disabled")
            self.scoreEntry.config(state="normal")
        self.logger.info("score mode changed to " + self.scoreMode.get())


    def ok(self) -> None:
        self.logger.info(f"OK button clicked, score mode: {self.scoreMode.get()}, reason mode: {self.reasonMode.get()}, number: {self.scoreValue.get()}")
        scoresJson = util.getJsonData("scores")
        infoJson = util.getJsonData("info")
        for i in range(1, len(util.getJsonData("students")) + 1):
            if self.checkbuttonNumberStatus[str(i)].get():
                if self.scoreMode.get() == "addorsub":
                    if self.scoreSymbol.get() == "+":
                        scoresJson[str(i)] += self.scoreValue.get()
                    else:
                        scoresJson[str(i)] -= self.scoreValue.get()
                    infoJson["data"].append(
                        {
                            "学号": str(i),
                            "分数变化": self.scoreSymbol.get() + str(self.scoreValue.get()),
                            "当前分数": scoresJson[str(i)],
                            "原因": self.reasonText.get(),
                            "时间": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                        }
                    )
                else:
                    scoresJson[str(i)] = self.scoreEntry.get()
                    infoJson["data"].append(
                        {
                            "学号": str(i),
                            "分数变化": f"直接修改为{self.scoreEntry.get()}",
                            "当前分数": scoresJson[str(i)],
                            "原因": self.reasonText.get(),
                            "时间": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        }
                    )
        scoresJson.write()
        infoJson.write()
        messagebox.showinfo("提示", "分数加/减成功！")
        self.logger.info("score operation has done!")


class editScoreFrame(object): ...


#     def __init__(self, master):
#         self.master = master
#         self.win = Frame(self.master)
#         self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

#         label1 = Label(self.win, text='修改分数界面')
#         label1.pack()

#         label2 = Label(self.win, text='学号')
#         label2.place(relx=0, rely=0.1)

#         label3 = Label(self.win, text='修改的分数')
#         label3.place(relx=0.7, rely=0.1)

#         label4 = Label(self.win, text='修改分数原因')
#         label4.place(relx=0.7, rely=0.4)

#         self.csbv_dict = {}
#         self.csb_dict = {}

#         self.csb_dict['1'] = Checkbutton(self.win, text='1', command=lambda: self.set_value('1'))

#         entry1 = Entry(self.win)
#         entry1.place(relx=0.7, rely=0.2, relwidth=0.3)

#         entry2 = Entry(self.win)
#         entry2.place(relx=0.7, rely=0.5, relwidth=0.3)

#         button1 = Button(self.win, text='返回', command=self.back)
#         button1.place(relx=0, rely=0.9, relwidth=0.2)

#         button2 = Button(self.win, text='确定', command=lambda: self.yes(entry1, entry2))
#         button2.place(relx=0.8, rely=0.9, relwidth=0.2)

#     # def back(self):
#     #     self.win.destroy()
#     #     main_window(self.master)

#     # def set_value(self, value):
#     #     if self.csbv_dict[value] == 0:
#     #         self.csbv_dict[value] = 1
#     #     else:
#     #         self.csbv_dict[value] = 0
#     #     print(self.csbv_dict[value])

#     # def set_all(self):
#     #     all_value = self.csbv_dict['all']
#     #     if all_value == 0:
#     #         for num in self.csb_dict.keys():
#     #             self.csb_dict[num].config(state=DISABLED)
#     #         self.csb_dict['all'].config(state=NORMAL)
#     #         self.csbv_dict['all'] = 1
#     #     else:
#     #         for num in self.csb_dict.keys():
#     #             self.csb_dict[num].config(state=NORMAL)
#     #         self.csbv_dict['all'] = 0

#     # def yes(self, entry1, entry2):
#     #     global class_info
#     #     get_num = int(entry1.get())
#     #     get_info = entry2.get()
#     #     if self.csbv_dict['all'] == 1:
#     #         for nums in self.csbv_dict.keys():
#     #             if nums != 'all':
#     #                 class_info[nums]['总分'] = get_num
#     #                 time = ti.localtime()
#     #                 class_info[nums]['今日加减分数原因'].append(f'{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒' + get_info + ' 修改分数为{}'.format(str(get_num)))
#     #             else:
#     #                 pass
#     #     else:
#     #         for nums in self.csbv_dict.keys():
#     #             if nums != 'all' and self.csbv_dict[nums] == 1:
#     #                 class_info[nums]['总分'] = get_num
#     #                 time = ti.localtime()
#     #                 class_info[nums]['今日加减分数原因'].append(f'{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒' + get_info + ' 修改分数为{}'.format(str(get_num)))
#     #             else:
#     #                 pass
#     #     user_name = getusername.getuser()
#     #     with open(file=r'C:\Users\{}\.class\class_info.json'.format(user_name), mode='w', encoding='utf-8') as f:
#     #         f.write(str(class_info))
#     #         f.close()
#     #     showinfo(title='提示', message='修改分数成功！')


class searchFrame(object): ...


#     def __init__(self, master):
#         self.master = master
#         self.win = Frame(self.master)
#         self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

#         label1 = Label(self.win, text='查询分数界面')
#         label1.pack()

#         label2 = Label(self.win, text='输入学号')
#         label2.place(relx=0, rely=0.1)

#         entry1 = Entry(self.win)
#         entry1.place(relx=0.2, rely=0.1, relwidth=0.6)

#         text1 = Text(self.win)
#         text1.place(relx=0, rely=0.2, relwidth=1, relheight=0.7)
#         text1.delete(0.0, END)
#         for key, value in class_info.items():
#             if key != 'time':
#                 text1.insert(END, key + str(value) + '\n')

#         button1 = Button(self.win, text='查询', command=lambda: self.search(entry1, text1))
#         button1.place(relx=0.8, rely=0.1, relwidth=0.2)

#         button2 = Button(self.win, text='返回', command=self.back)
#         button2.place(relx=0, rely=0.9, relwidth=0.2)

#     # def back(self):
#     #     self.win.destroy()
#     #     main_window(self.master)

#     # def search(self, entry1, text1):
#     #     get_num = entry1.get()
#     #     if get_num != '':
#     #         for nums in class_info.keys():
#     #             if nums == get_num:
#     #                 text1.delete(0.0, END)
#     #                 text1.insert(END, class_info[nums])
#     #                 break
#     #     else:
#     #         text1.delete(0.0, END)
#     #         for key, value in class_info.items():
#     #             if key != 'time':
#     #                 text1.insert(END, key + str(value) + '\n')


class rankFrame(object): ...


#     def __init__(self, master):
#         self.master = master
#         self.win = Frame(self.master)
#         self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

#         label1 = Label(self.win, text='排行榜')
#         label1.pack()

#         num_list = []
#         for num in range(1, 51):
#             num_list.append(str(num))

#         score_list = []
#         for num in range(1, 51):
#             if num in [4, 20, 26, 33, 46]:
#                 score_list.append(0)
#             else:
#                 score_list.append(class_info[str(num)]['总分'])

#         pack_list = list(zip(num_list, score_list))
#         print(pack_list)

#         for i in range(len(pack_list) - 1):
#             for j in range(len(pack_list) - i - 1):
#                 if pack_list[j][1] < pack_list[j + 1][1]:
#                     pack_list[j], pack_list[j + 1] = pack_list[j + 1], pack_list[j]
#         print(pack_list)

#         text1 = Text(self.win)
#         text1.place(relx=0, rely=0.2, relwidth=1, relheight=0.7)

#         for i in range(len(pack_list)):
#             if pack_list[i][0] in ['4', '20', '26', '33', '46', 'time']:
#                 pass
#             else:
#                 text1.insert(END, '第{}名：'.format(i + 1) + pack_list[i][0] + '号' + str(class_info[pack_list[i][0]]) + '\n')

#         label2 = Label(self.win, text='输入字符（本查找为范围性查找）')
#         label2.place(relx=0, rely=0.1, relwidth=0.3)

#         entry1 = Entry(self.win)
#         entry1.place(relx=0.3, rely=0.1, relwidth=0.5)

#         button1 = Button(self.win, text='查询', command=lambda: self.search(text1, entry1))
#         button1.place(relx=0.8, relwidth=0.2, rely=0.1)

#         button2 = Button(self.win, text='返回', command=self.back)
#         button2.place(relx=0, rely=0.9, relwidth=0.2)

#         button3 = Button(self.win, text='导出', command=lambda: self.out(pack_list))
#         button3.place(relx=0.8, rely=0.9, relwidth=0.2)

#     # def back(self):
#     #     self.win.destroy()
#     #     main_window(self.master)

#     # def out(self, pack_list):
#     #     file = asksaveasfilename(title='导出文件', initialdir='C:\\', filetypes=[('txt文本文档', '*.txt'), ('excel（暂时不支持）', '*.xlsx'), ('全部文件', '*.*')], defaultextension='*.txt')

#     #     if file:
#     #         with open(file=file, mode='a+', encoding='utf-8') as f:
#     #             for i in range(len(pack_list)):
#     #                 if pack_list[i][0] in ['4', '20', '26', '33', '46', 'time']:
#     #                     pass
#     #                 else:
#     #                     f.write(pack_list[i][0] + '的总分是：{}，今日加减分数是：{}，今日加减分数原因是：{}\n'.format(str(class_info[pack_list[i][0]]['总分']), str(class_info[pack_list[i][0]]['加减分数']), str(class_info[pack_list[i][0]]['今日加减分数原因'])))
#     #         showinfo(title='提示', message='导出成功！')

#     # def search(self, text1, entry1):
#     #     text_temp = text1.get(0.0, END)
#     #     entry_text = entry1.get()
#     #     text = text_temp.split('\n')
#     #     search_list = []
#     #     if entry_text == '':
#     #         pass
#     #     else:
#     #         for i in range(len(text)):
#     #             if entry_text in text[i]:
#     #                 search_list.append(text[i])
#     #     text1.delete(0.0, END)
#     #     for item in search_list:
#     #         text1.insert(END, item + '\n')


class randomStudentFrame(object): ...


class searchStudentFrame(object): ...


class timerFrame(object): ...


class aboutFrame(object): ...
