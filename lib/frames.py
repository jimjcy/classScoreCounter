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


class initWindow(tk.Tk):
    """Init window of the program"""

    def __init__(self) -> None:
        super().__init__()
        self.geometry("500x500")
        self.title("班级管理工具")


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

        self.writeButton = ttk.Button(
            self.frame,
            text="直接修改",
            command=lambda: util.toFrame(self.master, self.frame, editScoreFrame),
        )
        self.writeButton.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.1)

        self.searchButton = ttk.Button(
            self.frame,
            text="查询",
            command=lambda: util.toFrame(self.master, self.frame, searchFrame),
        )
        self.searchButton.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.1)

        self.rankButton = ttk.Button(
            self.frame,
            text="排行榜",
            command=lambda: util.toFrame(self.master, self.frame, rankFrame),
        )
        self.rankButton.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.1)

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


class ScoreFrame(object):
    def __init__(self, master: tk.Tk) -> None:
        self.checkbuttonDict: Dict[str, ttk.Checkbutton] = {}
        self.checkbuttonStatus: Dict[str, tk.BooleanVar] = {"all": tk.BooleanVar()}
        self.scoreSymbol = tk.StringVar()
        self.scoreValue = tk.IntVar()
        self.reasonMode = tk.StringVar()
        self.reasonText = tk.StringVar()
        self.master = master

        self.studentNumberFrame = ttk.Frame(self.master)
        self.studentNumberFrame.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        self.scoreFrame = ttk.Frame(self.master)
        self.scoreFrame.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)

        self.frameName = ttk.Label(self.studentNumberFrame, text="管理分数界面")
        self.frameName.place(relx=0.7)

        self.studentNumberLabel = ttk.Label(self.studentNumberFrame, text="学号面板")
        self.studentNumberLabel.place(relx=0, rely=0.05)

        self.backButton = ttk.Button(
            self.studentNumberFrame,
            text="返回",
            command=lambda: util.toFrame(
                self.master, [self.studentNumberFrame, self.scoreFrame], mainFrame
            ),
        )
        self.backButton.place(relx=0, rely=0.9, relheight=0.1)

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
                    functools.partial(self.setValue, (i - 1) * 10 + j),
                )
                checkButton.place(
                    relx=(i - 1) / 10 + 0.05 * (i - 1), rely=j / 10 - 0.03 * (j - 1)
                )
                self.checkbuttonStatus[str((i - 1) * 10 + j)] = boolvar
                self.checkbuttonDict[str((i - 1) * 10 + j)] = checkButton

        self.checkbuttonDict["all"] = util.createCheckButton(
            self.studentNumberFrame, "全选", self.checkbuttonStatus["all"], self.setAll
        )
        self.checkbuttonDict["all"].place(relx=0.75, rely=0.24)
        self.checkbuttonStatus["all"].set(False)

        self.scoreLabel = ttk.Label(self.scoreFrame, text="分数面板")
        self.scoreLabel.place(relx=0, rely=0.1)

        self.scoreSymbolCombobox = ttk.Combobox(
            self.scoreFrame, textvariable=self.scoreSymbol
        )
        self.scoreSymbolCombobox["values"] = ["+", "-"]
        self.scoreSymbolCombobox.place(relx=0, rely=0.2, relwidth=0.4)
        self.scoreSymbolCombobox.current(0)

        self.scoreValueCombobox = ttk.Combobox(
            self.scoreFrame, textvariable=self.scoreValue
        )
        self.scoreValueCombobox["values"] = [x for x in range(1, 11)]
        self.scoreValueCombobox.place(relx=0.4, rely=0.2, relwidth=0.6)
        self.scoreValueCombobox.current(0)

        self.reasonLabel = ttk.Label(self.scoreFrame, text="加分原因")
        self.reasonLabel.place(relx=0, rely=0.3)

        self.reasonRadiobutton1 = ttk.Radiobutton(
            self.scoreFrame,
            variable=self.reasonMode,
            value="json",
            command=self.setMode,
        )
        self.reasonRadiobutton1.place(relx=0, rely=0.4)

        self.reasonCombobox = ttk.Combobox(
            self.scoreFrame, textvariable=self.reasonText
        )
        self.reasonCombobox["values"] = util.getJsonData("reasons")["reasons"]
        self.reasonCombobox.place(relx=0.2, rely=0.4, relwidth=0.8)
        self.reasonCombobox.current(0)

        self.reasonRadiobutton2 = ttk.Radiobutton(
            self.scoreFrame,
            variable=self.reasonMode,
            value="input",
            command=self.setMode,
        )
        self.reasonRadiobutton2.place(relx=0, rely=0.5)

        self.reasonEntry = ttk.Entry(self.scoreFrame, textvariable=self.reasonText)
        self.reasonEntry.place(relx=0.2, rely=0.5, relwidth=0.8)
        self.reasonEntry.config(state="disabled")

        self.reasonRadiobutton3 = ttk.Radiobutton(
            self.scoreFrame,
            variable=self.reasonMode,
            value="none",
            command=self.setMode,
        )
        self.reasonRadiobutton3.place(relx=0, rely=0.6)

        self.reasonNoneLabel = ttk.Label(self.scoreFrame, text="无")
        self.reasonNoneLabel.place(relx=0.2, rely=0.6)

        self.reasonMode.set("json")

        self.yesButton = ttk.Button(
            self.scoreFrame,
            text="确定",
            command=self.ok
        )
        self.yesButton.place(relx=0.6, rely=0.9, relheight=0.1)

    def setValue(
        self, index: Union[str, int], toIndex: Union[str, int, None] = None
    ) -> None:
        if toIndex is None:
            toIndex = index
        self.checkbuttonStatus[str(index)].set(self.checkbuttonStatus[str(toIndex)].get())

    def setAll(self) -> None:
        for i in range(1, len(self.checkbuttonDict)):
            self.setValue(str(i), "all")

    def setMode(self) -> None:
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
            self.reasonText.set("")
    
    def ok(self) -> None:
        scoresJson: dict = {}
        infoJson: dict = util.getJsonData("info")
        __scoresIO = open(
            pathlib.Path(os.getcwd()).joinpath("data").joinpath("scores.json"),
            "r",
            encoding="utf-8",
        )
        try:
            scoresJson = json.loads(__scoresIO.read())
        except json.decoder.JSONDecodeError:
            scoresJson = {}
            for i in range(1, len(util.getJsonData("students")) + 1):
                scoresJson[str(i)] = 0
        __scoresIO.close()
        __scoresIO = open(
            pathlib.Path(os.getcwd()).joinpath("data").joinpath("info.json"),
            "w",
            encoding="utf-8",
        )
        __infoIO = open(
            pathlib.Path(os.getcwd()).joinpath("data").joinpath("info.json"),
            "w",
            encoding="utf-8",
        )
        for i in range(1, len(util.getJsonData("students")) + 1):
            if self.checkbuttonStatus[str(i)].get():
                if self.scoreSymbol.get() == "+":
                    scoresJson[str(i)] += self.scoreValue.get()
                else:
                    scoresJson[str(i)] -= self.scoreValue.get()
                infoJson["data"].append({
                    "学号": str(i),
                    "分数变化": self.scoreSymbol.get() + str(self.scoreValue.get()),
                    "当前分数": scoresJson[str(i)],
                    "原因": self.reasonText.get(),
                    "时间": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                })
        __scoresIO.write(json.dumps(scoresJson))
        __infoIO.write(json.dumps(infoJson))
        __scoresIO.close()
        __infoIO.close()
        messagebox.showinfo("提示", "分数加/减成功！")


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