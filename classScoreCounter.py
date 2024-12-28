# -*- coding: utf-8 -*-
import os as o
import time
import lib.frames as frames


class add:
    def __init__(self, master):
        self.master = master
        self.win = Frame(self.master)
        self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

        label1 = Label(self.win, text='加分界面')
        label1.pack()

        label2 = Label(self.win, text='学号')
        label2.place(relx=0, rely=0.1)

        label3 = Label(self.win, text='加的分数')
        label3.place(relx=0.7, rely=0.1)

        label4 = Label(self.win, text='加分原因')
        label4.place(relx=0.7, rely=0.4)

        self.csbv_dict = {}
        self.csb_dict = {}
        for num in range(1, 51):
            if num == 4:
                pass
            elif num == 20:
                pass
            elif num == 26:
                pass
            elif num == 33:
                pass
            elif num == 46:
                pass
            else:
                self.csbv_dict[str(num)] = 0
        self.csbv_dict['all'] = 0

        self.csb_dict['1'] = Checkbutton(self.win, text='1', command=lambda: self.set_value('1'))
        self.csb_dict['2'] = Checkbutton(self.win, text='2', command=lambda: self.set_value('2'))
        self.csb_dict['3'] = Checkbutton(self.win, text='3', command=lambda: self.set_value('3'))
        self.csb_dict['5'] = Checkbutton(self.win, text='5', command=lambda: self.set_value('4'))
        self.csb_dict['6'] = Checkbutton(self.win, text='6', command=lambda: self.set_value('5'))
        self.csb_dict['7'] = Checkbutton(self.win, text='7', command=lambda: self.set_value('7'))
        self.csb_dict['8'] = Checkbutton(self.win, text='8', command=lambda: self.set_value('8'))
        self.csb_dict['9'] = Checkbutton(self.win, text='9', command=lambda: self.set_value('9'))
        self.csb_dict['10'] = Checkbutton(self.win, text='10', command=lambda: self.set_value('10'))
        self.csb_dict['11'] = Checkbutton(self.win, text='11', command=lambda: self.set_value('11'))
        self.csb_dict['12'] = Checkbutton(self.win, text='12', command=lambda: self.set_value('12'))
        self.csb_dict['13'] = Checkbutton(self.win, text='13', command=lambda: self.set_value('13'))
        self.csb_dict['14'] = Checkbutton(self.win, text='14', command=lambda: self.set_value('14'))
        self.csb_dict['15'] = Checkbutton(self.win, text='15', command=lambda: self.set_value('15'))
        self.csb_dict['16'] = Checkbutton(self.win, text='16', command=lambda: self.set_value('16'))
        self.csb_dict['17'] = Checkbutton(self.win, text='17', command=lambda: self.set_value('17'))
        self.csb_dict['18'] = Checkbutton(self.win, text='18', command=lambda: self.set_value('18'))
        self.csb_dict['19'] = Checkbutton(self.win, text='19', command=lambda: self.set_value('19'))
        self.csb_dict['21'] = Checkbutton(self.win, text='21', command=lambda: self.set_value('21'))
        self.csb_dict['22'] = Checkbutton(self.win, text='22', command=lambda: self.set_value('22'))
        self.csb_dict['23'] = Checkbutton(self.win, text='23', command=lambda: self.set_value('23'))
        self.csb_dict['24'] = Checkbutton(self.win, text='24', command=lambda: self.set_value('24'))
        self.csb_dict['25'] = Checkbutton(self.win, text='25', command=lambda: self.set_value('25'))
        self.csb_dict['27'] = Checkbutton(self.win, text='27', command=lambda: self.set_value('27'))
        self.csb_dict['28'] = Checkbutton(self.win, text='28', command=lambda: self.set_value('28'))
        self.csb_dict['29'] = Checkbutton(self.win, text='29', command=lambda: self.set_value('29'))
        self.csb_dict['30'] = Checkbutton(self.win, text='30', command=lambda: self.set_value('30'))
        self.csb_dict['31'] = Checkbutton(self.win, text='31', command=lambda: self.set_value('31'))
        self.csb_dict['32'] = Checkbutton(self.win, text='32', command=lambda: self.set_value('32'))
        self.csb_dict['34'] = Checkbutton(self.win, text='34', command=lambda: self.set_value('34'))
        self.csb_dict['35'] = Checkbutton(self.win, text='35', command=lambda: self.set_value('35'))
        self.csb_dict['36'] = Checkbutton(self.win, text='36', command=lambda: self.set_value('36'))
        self.csb_dict['37'] = Checkbutton(self.win, text='37', command=lambda: self.set_value('37'))
        self.csb_dict['38'] = Checkbutton(self.win, text='38', command=lambda: self.set_value('38'))
        self.csb_dict['39'] = Checkbutton(self.win, text='39', command=lambda: self.set_value('39'))
        self.csb_dict['40'] = Checkbutton(self.win, text='40', command=lambda: self.set_value('40'))
        self.csb_dict['41'] = Checkbutton(self.win, text='41', command=lambda: self.set_value('41'))
        self.csb_dict['42'] = Checkbutton(self.win, text='42', command=lambda: self.set_value('42'))
        self.csb_dict['43'] = Checkbutton(self.win, text='43', command=lambda: self.set_value('43'))
        self.csb_dict['44'] = Checkbutton(self.win, text='44', command=lambda: self.set_value('44'))
        self.csb_dict['45'] = Checkbutton(self.win, text='45', command=lambda: self.set_value('45'))
        self.csb_dict['47'] = Checkbutton(self.win, text='47', command=lambda: self.set_value('47'))
        self.csb_dict['48'] = Checkbutton(self.win, text='48', command=lambda: self.set_value('48'))
        self.csb_dict['49'] = Checkbutton(self.win, text='49', command=lambda: self.set_value('49'))
        self.csb_dict['50'] = Checkbutton(self.win, text='50', command=lambda: self.set_value('50'))
        self.csb_dict['all'] = Checkbutton(self.win, text='全选', command=self.set_all)

        i = 0.2
        for csb in self.csb_dict.keys():
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[7:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.1, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[14:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.2, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[21:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.3, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[28:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.4, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[35:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.5, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[42:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.6, rely=i)
                i += 0.1

        entry1 = Entry(self.win)
        entry1.place(relx=0.7, rely=0.2, relwidth=0.3)

        entry2 = Entry(self.win)
        entry2.place(relx=0.7, rely=0.5, relwidth=0.3)

        button1 = Button(self.win, text='返回', command=self.back)
        button1.place(relx=0, rely=0.9, relwidth=0.2)

        button2 = Button(self.win, text='确定', command=lambda: self.yes(entry1, entry2))
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
        all_value = self.csbv_dict['all']
        if all_value == 0:
            for num in self.csb_dict.keys():
                self.csb_dict[num].config(state=DISABLED)
            self.csb_dict['all'].config(state=NORMAL)
            self.csbv_dict['all'] = 1
        else:
            for num in self.csb_dict.keys():
                self.csb_dict[num].config(state=NORMAL)
            self.csbv_dict['all'] = 0

    def yes(self, entry1, entry2):
        global class_info
        get_num = int(entry1.get())
        get_info = entry2.get()
        if self.csbv_dict['all'] == 1:
            for nums in self.csbv_dict.keys():
                if nums != 'all':
                    class_info[nums]['总分'] += get_num
                    class_info[nums]['加减分数'] += get_num
                    time = ti.localtime()
                    class_info[nums]['今日加减分数原因'].append(f'{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒' + get_info + ' +{}'.format(str(get_num)))
                else:
                    pass
        else:
            for nums in self.csbv_dict.keys():
                if nums != 'all' and self.csbv_dict[nums] == 1:
                    class_info[nums]['总分'] += get_num
                    class_info[nums]['加减分数'] += get_num
                    time = ti.localtime()
                    class_info[nums]['今日加减分数原因'].append(f'{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒' + get_info + ' +{}'.format(str(get_num)))
                else:
                    pass
        user_name = getusername.getuser()
        with open(file=r'C:\Users\{}\.class\class_info.json'.format(user_name), mode='w', encoding='utf-8') as f:
            f.write(str(class_info))
            f.close()
        showinfo(title='提示', message='加分成功！')


class delete:
    def __init__(self, master):
        self.master = master
        self.win = Frame(self.master)
        self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

        label1 = Label(self.win, text='减分界面')
        label1.pack()

        label2 = Label(self.win, text='学号')
        label2.place(relx=0, rely=0.1)

        label3 = Label(self.win, text='减的分数')
        label3.place(relx=0.7, rely=0.1)

        label4 = Label(self.win, text='减分原因')
        label4.place(relx=0.7, rely=0.4)

        self.csbv_dict = {}
        self.csb_dict = {}
        for num in range(1, 51):
            if num == 4:
                pass
            elif num == 20:
                pass
            elif num == 26:
                pass
            elif num == 33:
                pass
            elif num == 46:
                pass
            else:
                self.csbv_dict[str(num)] = 0
        self.csbv_dict['all'] = 0

        self.csb_dict['1'] = Checkbutton(self.win, text='1', command=lambda: self.set_value('1'))
        self.csb_dict['2'] = Checkbutton(self.win, text='2', command=lambda: self.set_value('2'))
        self.csb_dict['3'] = Checkbutton(self.win, text='3', command=lambda: self.set_value('3'))
        self.csb_dict['5'] = Checkbutton(self.win, text='5', command=lambda: self.set_value('4'))
        self.csb_dict['6'] = Checkbutton(self.win, text='6', command=lambda: self.set_value('5'))
        self.csb_dict['7'] = Checkbutton(self.win, text='7', command=lambda: self.set_value('7'))
        self.csb_dict['8'] = Checkbutton(self.win, text='8', command=lambda: self.set_value('8'))
        self.csb_dict['9'] = Checkbutton(self.win, text='9', command=lambda: self.set_value('9'))
        self.csb_dict['10'] = Checkbutton(self.win, text='10', command=lambda: self.set_value('10'))
        self.csb_dict['11'] = Checkbutton(self.win, text='11', command=lambda: self.set_value('11'))
        self.csb_dict['12'] = Checkbutton(self.win, text='12', command=lambda: self.set_value('12'))
        self.csb_dict['13'] = Checkbutton(self.win, text='13', command=lambda: self.set_value('13'))
        self.csb_dict['14'] = Checkbutton(self.win, text='14', command=lambda: self.set_value('14'))
        self.csb_dict['15'] = Checkbutton(self.win, text='15', command=lambda: self.set_value('15'))
        self.csb_dict['16'] = Checkbutton(self.win, text='16', command=lambda: self.set_value('16'))
        self.csb_dict['17'] = Checkbutton(self.win, text='17', command=lambda: self.set_value('17'))
        self.csb_dict['18'] = Checkbutton(self.win, text='18', command=lambda: self.set_value('18'))
        self.csb_dict['19'] = Checkbutton(self.win, text='19', command=lambda: self.set_value('19'))
        self.csb_dict['21'] = Checkbutton(self.win, text='21', command=lambda: self.set_value('21'))
        self.csb_dict['22'] = Checkbutton(self.win, text='22', command=lambda: self.set_value('22'))
        self.csb_dict['23'] = Checkbutton(self.win, text='23', command=lambda: self.set_value('23'))
        self.csb_dict['24'] = Checkbutton(self.win, text='24', command=lambda: self.set_value('24'))
        self.csb_dict['25'] = Checkbutton(self.win, text='25', command=lambda: self.set_value('25'))
        self.csb_dict['27'] = Checkbutton(self.win, text='27', command=lambda: self.set_value('27'))
        self.csb_dict['28'] = Checkbutton(self.win, text='28', command=lambda: self.set_value('28'))
        self.csb_dict['29'] = Checkbutton(self.win, text='29', command=lambda: self.set_value('29'))
        self.csb_dict['30'] = Checkbutton(self.win, text='30', command=lambda: self.set_value('30'))
        self.csb_dict['31'] = Checkbutton(self.win, text='31', command=lambda: self.set_value('31'))
        self.csb_dict['32'] = Checkbutton(self.win, text='32', command=lambda: self.set_value('32'))
        self.csb_dict['34'] = Checkbutton(self.win, text='34', command=lambda: self.set_value('34'))
        self.csb_dict['35'] = Checkbutton(self.win, text='35', command=lambda: self.set_value('35'))
        self.csb_dict['36'] = Checkbutton(self.win, text='36', command=lambda: self.set_value('36'))
        self.csb_dict['37'] = Checkbutton(self.win, text='37', command=lambda: self.set_value('37'))
        self.csb_dict['38'] = Checkbutton(self.win, text='38', command=lambda: self.set_value('38'))
        self.csb_dict['39'] = Checkbutton(self.win, text='39', command=lambda: self.set_value('39'))
        self.csb_dict['40'] = Checkbutton(self.win, text='40', command=lambda: self.set_value('40'))
        self.csb_dict['41'] = Checkbutton(self.win, text='41', command=lambda: self.set_value('41'))
        self.csb_dict['42'] = Checkbutton(self.win, text='42', command=lambda: self.set_value('42'))
        self.csb_dict['43'] = Checkbutton(self.win, text='43', command=lambda: self.set_value('43'))
        self.csb_dict['44'] = Checkbutton(self.win, text='44', command=lambda: self.set_value('44'))
        self.csb_dict['45'] = Checkbutton(self.win, text='45', command=lambda: self.set_value('45'))
        self.csb_dict['47'] = Checkbutton(self.win, text='47', command=lambda: self.set_value('47'))
        self.csb_dict['48'] = Checkbutton(self.win, text='48', command=lambda: self.set_value('48'))
        self.csb_dict['49'] = Checkbutton(self.win, text='49', command=lambda: self.set_value('49'))
        self.csb_dict['50'] = Checkbutton(self.win, text='50', command=lambda: self.set_value('50'))
        self.csb_dict['all'] = Checkbutton(self.win, text='全选', command=self.set_all)

        i = 0.2
        for csb in self.csb_dict.keys():
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[7:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.1, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[14:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.2, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[21:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.3, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[28:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.4, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[35:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.5, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[42:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.6, rely=i)
                i += 0.1

        entry1 = Entry(self.win)
        entry1.place(relx=0.7, rely=0.2, relwidth=0.3)

        entry2 = Entry(self.win)
        entry2.place(relx=0.7, rely=0.5, relwidth=0.3)

        button1 = Button(self.win, text='返回', command=self.back)
        button1.place(relx=0, rely=0.9, relwidth=0.2)

        button2 = Button(self.win, text='确定', command=lambda: self.yes(entry1, entry2))
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
        all_value = self.csbv_dict['all']
        if all_value == 0:
            for num in self.csb_dict.keys():
                self.csb_dict[num].config(state=DISABLED)
            self.csb_dict['all'].config(state=NORMAL)
            self.csbv_dict['all'] = 1
        else:
            for num in self.csb_dict.keys():
                self.csb_dict[num].config(state=NORMAL)
            self.csbv_dict['all'] = 0

    def yes(self, entry1, entry2):
        global class_info
        get_num = int(entry1.get())
        get_info = entry2.get()
        if self.csbv_dict['all'] == 1:
            for nums in self.csbv_dict.keys():
                if nums != 'all':
                    class_info[nums]['总分'] -= get_num
                    class_info[nums]['加减分数'] -= get_num
                    time = ti.localtime()
                    class_info[nums]['今日加减分数原因'].append(f'{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒' + get_info + ' -{}'.format(str(get_num)))
                else:
                    pass
        else:
            for nums in self.csbv_dict.keys():
                if nums != 'all' and self.csbv_dict[nums] == 1:
                    class_info[nums]['总分'] -= get_num
                    class_info[nums]['加减分数'] -= get_num
                    time = ti.localtime()
                    class_info[nums]['今日加减分数原因'].append(f'{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒' + get_info + ' -{}'.format(str(get_num)))
                else:
                    pass
        user_name = getusername.getuser()
        with open(file=r'C:\Users\{}\.class\class_info.json'.format(user_name), mode='w', encoding='utf-8') as f:
            f.write(str(class_info))
            f.close()
        showinfo(title='提示', message='减分成功！')


class write:
    def __init__(self, master):
        self.master = master
        self.win = Frame(self.master)
        self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

        label1 = Label(self.win, text='修改分数界面')
        label1.pack()

        label2 = Label(self.win, text='学号')
        label2.place(relx=0, rely=0.1)

        label3 = Label(self.win, text='修改的分数')
        label3.place(relx=0.7, rely=0.1)

        label4 = Label(self.win, text='修改分数原因')
        label4.place(relx=0.7, rely=0.4)

        self.csbv_dict = {}
        self.csb_dict = {}
        for num in range(1, 51):
            if num == 4:
                pass
            elif num == 20:
                pass
            elif num == 26:
                pass
            elif num == 33:
                pass
            elif num == 46:
                pass
            else:
                self.csbv_dict[str(num)] = 0
        self.csbv_dict['all'] = 0

        self.csb_dict['1'] = Checkbutton(self.win, text='1', command=lambda: self.set_value('1'))
        self.csb_dict['2'] = Checkbutton(self.win, text='2', command=lambda: self.set_value('2'))
        self.csb_dict['3'] = Checkbutton(self.win, text='3', command=lambda: self.set_value('3'))
        self.csb_dict['5'] = Checkbutton(self.win, text='5', command=lambda: self.set_value('4'))
        self.csb_dict['6'] = Checkbutton(self.win, text='6', command=lambda: self.set_value('5'))
        self.csb_dict['7'] = Checkbutton(self.win, text='7', command=lambda: self.set_value('7'))
        self.csb_dict['8'] = Checkbutton(self.win, text='8', command=lambda: self.set_value('8'))
        self.csb_dict['9'] = Checkbutton(self.win, text='9', command=lambda: self.set_value('9'))
        self.csb_dict['10'] = Checkbutton(self.win, text='10', command=lambda: self.set_value('10'))
        self.csb_dict['11'] = Checkbutton(self.win, text='11', command=lambda: self.set_value('11'))
        self.csb_dict['12'] = Checkbutton(self.win, text='12', command=lambda: self.set_value('12'))
        self.csb_dict['13'] = Checkbutton(self.win, text='13', command=lambda: self.set_value('13'))
        self.csb_dict['14'] = Checkbutton(self.win, text='14', command=lambda: self.set_value('14'))
        self.csb_dict['15'] = Checkbutton(self.win, text='15', command=lambda: self.set_value('15'))
        self.csb_dict['16'] = Checkbutton(self.win, text='16', command=lambda: self.set_value('16'))
        self.csb_dict['17'] = Checkbutton(self.win, text='17', command=lambda: self.set_value('17'))
        self.csb_dict['18'] = Checkbutton(self.win, text='18', command=lambda: self.set_value('18'))
        self.csb_dict['19'] = Checkbutton(self.win, text='19', command=lambda: self.set_value('19'))
        self.csb_dict['21'] = Checkbutton(self.win, text='21', command=lambda: self.set_value('21'))
        self.csb_dict['22'] = Checkbutton(self.win, text='22', command=lambda: self.set_value('22'))
        self.csb_dict['23'] = Checkbutton(self.win, text='23', command=lambda: self.set_value('23'))
        self.csb_dict['24'] = Checkbutton(self.win, text='24', command=lambda: self.set_value('24'))
        self.csb_dict['25'] = Checkbutton(self.win, text='25', command=lambda: self.set_value('25'))
        self.csb_dict['27'] = Checkbutton(self.win, text='27', command=lambda: self.set_value('27'))
        self.csb_dict['28'] = Checkbutton(self.win, text='28', command=lambda: self.set_value('28'))
        self.csb_dict['29'] = Checkbutton(self.win, text='29', command=lambda: self.set_value('29'))
        self.csb_dict['30'] = Checkbutton(self.win, text='30', command=lambda: self.set_value('30'))
        self.csb_dict['31'] = Checkbutton(self.win, text='31', command=lambda: self.set_value('31'))
        self.csb_dict['32'] = Checkbutton(self.win, text='32', command=lambda: self.set_value('32'))
        self.csb_dict['34'] = Checkbutton(self.win, text='34', command=lambda: self.set_value('34'))
        self.csb_dict['35'] = Checkbutton(self.win, text='35', command=lambda: self.set_value('35'))
        self.csb_dict['36'] = Checkbutton(self.win, text='36', command=lambda: self.set_value('36'))
        self.csb_dict['37'] = Checkbutton(self.win, text='37', command=lambda: self.set_value('37'))
        self.csb_dict['38'] = Checkbutton(self.win, text='38', command=lambda: self.set_value('38'))
        self.csb_dict['39'] = Checkbutton(self.win, text='39', command=lambda: self.set_value('39'))
        self.csb_dict['40'] = Checkbutton(self.win, text='40', command=lambda: self.set_value('40'))
        self.csb_dict['41'] = Checkbutton(self.win, text='41', command=lambda: self.set_value('41'))
        self.csb_dict['42'] = Checkbutton(self.win, text='42', command=lambda: self.set_value('42'))
        self.csb_dict['43'] = Checkbutton(self.win, text='43', command=lambda: self.set_value('43'))
        self.csb_dict['44'] = Checkbutton(self.win, text='44', command=lambda: self.set_value('44'))
        self.csb_dict['45'] = Checkbutton(self.win, text='45', command=lambda: self.set_value('45'))
        self.csb_dict['47'] = Checkbutton(self.win, text='47', command=lambda: self.set_value('47'))
        self.csb_dict['48'] = Checkbutton(self.win, text='48', command=lambda: self.set_value('48'))
        self.csb_dict['49'] = Checkbutton(self.win, text='49', command=lambda: self.set_value('49'))
        self.csb_dict['50'] = Checkbutton(self.win, text='50', command=lambda: self.set_value('50'))
        self.csb_dict['all'] = Checkbutton(self.win, text='全选', command=self.set_all)

        i = 0.2
        for csb in self.csb_dict.keys():
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[7:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.1, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[14:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.2, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[21:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.3, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[28:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.4, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[35:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.5, rely=i)
                i += 0.1

        i = 0.2
        for csb in tuple(self.csb_dict.keys())[42:]:
            if i == 0.9:
                break
            else:
                self.csb_dict[csb].place(relx=0.6, rely=i)
                i += 0.1

        entry1 = Entry(self.win)
        entry1.place(relx=0.7, rely=0.2, relwidth=0.3)

        entry2 = Entry(self.win)
        entry2.place(relx=0.7, rely=0.5, relwidth=0.3)

        button1 = Button(self.win, text='返回', command=self.back)
        button1.place(relx=0, rely=0.9, relwidth=0.2)

        button2 = Button(self.win, text='确定', command=lambda: self.yes(entry1, entry2))
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
        all_value = self.csbv_dict['all']
        if all_value == 0:
            for num in self.csb_dict.keys():
                self.csb_dict[num].config(state=DISABLED)
            self.csb_dict['all'].config(state=NORMAL)
            self.csbv_dict['all'] = 1
        else:
            for num in self.csb_dict.keys():
                self.csb_dict[num].config(state=NORMAL)
            self.csbv_dict['all'] = 0

    def yes(self, entry1, entry2):
        global class_info
        get_num = int(entry1.get())
        get_info = entry2.get()
        if self.csbv_dict['all'] == 1:
            for nums in self.csbv_dict.keys():
                if nums != 'all':
                    class_info[nums]['总分'] = get_num
                    time = ti.localtime()
                    class_info[nums]['今日加减分数原因'].append(f'{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒' + get_info + ' 修改分数为{}'.format(str(get_num)))
                else:
                    pass
        else:
            for nums in self.csbv_dict.keys():
                if nums != 'all' and self.csbv_dict[nums] == 1:
                    class_info[nums]['总分'] = get_num
                    time = ti.localtime()
                    class_info[nums]['今日加减分数原因'].append(f'{time[0]}年{time[1]}月{time[2]}日 {time[3]}时{time[4]}分{time[5]}秒' + get_info + ' 修改分数为{}'.format(str(get_num)))
                else:
                    pass
        user_name = getusername.getuser()
        with open(file=r'C:\Users\{}\.class\class_info.json'.format(user_name), mode='w', encoding='utf-8') as f:
            f.write(str(class_info))
            f.close()
        showinfo(title='提示', message='修改分数成功！')


class search:
    def __init__(self, master):
        self.master = master
        self.win = Frame(self.master)
        self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

        label1 = Label(self.win, text='查询分数界面')
        label1.pack()

        label2 = Label(self.win, text='输入学号')
        label2.place(relx=0, rely=0.1)

        entry1 = Entry(self.win)
        entry1.place(relx=0.2, rely=0.1, relwidth=0.6)

        text1 = Text(self.win)
        text1.place(relx=0, rely=0.2, relwidth=1, relheight=0.7)
        text1.delete(0.0, END)
        for key, value in class_info.items():
            if key != 'time':
                text1.insert(END, key + str(value) + '\n')

        button1 = Button(self.win, text='查询', command=lambda: self.search(entry1, text1))
        button1.place(relx=0.8, rely=0.1, relwidth=0.2)

        button2 = Button(self.win, text='返回', command=self.back)
        button2.place(relx=0, rely=0.9, relwidth=0.2)

    def back(self):
        self.win.destroy()
        main_window(self.master)

    def search(self, entry1, text1):
        get_num = entry1.get()
        if get_num != '':
            for nums in class_info.keys():
                if nums == get_num:
                    text1.delete(0.0, END)
                    text1.insert(END, class_info[nums])
                    break
        else:
            text1.delete(0.0, END)
            for key, value in class_info.items():
                if key != 'time':
                    text1.insert(END, key + str(value) + '\n')


class rank:
    def __init__(self, master):
        self.master = master
        self.win = Frame(self.master)
        self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

        label1 = Label(self.win, text='排行榜')
        label1.pack()

        num_list = []
        for num in range(1, 51):
            num_list.append(str(num))

        score_list = []
        for num in range(1, 51):
            if num in [4, 20, 26, 33, 46]:
                score_list.append(0)
            else:
                score_list.append(class_info[str(num)]['总分'])

        pack_list = list(zip(num_list, score_list))
        print(pack_list)

        for i in range(len(pack_list) - 1):
            for j in range(len(pack_list) - i - 1):
                if pack_list[j][1] < pack_list[j + 1][1]:
                    pack_list[j], pack_list[j + 1] = pack_list[j + 1], pack_list[j]
        print(pack_list)

        text1 = Text(self.win)
        text1.place(relx=0, rely=0.2, relwidth=1, relheight=0.7)

        for i in range(len(pack_list)):
            if pack_list[i][0] in ['4', '20', '26', '33', '46', 'time']:
                pass
            else:
                text1.insert(END, '第{}名：'.format(i + 1) + pack_list[i][0] + '号' + str(class_info[pack_list[i][0]]) + '\n')

        label2 = Label(self.win, text='输入字符（本查找为范围性查找）')
        label2.place(relx=0, rely=0.1, relwidth=0.3)

        entry1 = Entry(self.win)
        entry1.place(relx=0.3, rely=0.1, relwidth=0.5)

        button1 = Button(self.win, text='查询', command=lambda: self.search(text1, entry1))
        button1.place(relx=0.8, relwidth=0.2, rely=0.1)

        button2 = Button(self.win, text='返回', command=self.back)
        button2.place(relx=0, rely=0.9, relwidth=0.2)

        button3 = Button(self.win, text='导出', command=lambda: self.out(pack_list))
        button3.place(relx=0.8, rely=0.9, relwidth=0.2)

    def back(self):
        self.win.destroy()
        main_window(self.master)

    def out(self, pack_list):
        file = asksaveasfilename(title='导出文件', initialdir='C:\\', filetypes=[('txt文本文档', '*.txt'), ('excel（暂时不支持）', '*.xlsx'), ('全部文件', '*.*')], defaultextension='*.txt')

        if file:
            with open(file=file, mode='a+', encoding='utf-8') as f:
                for i in range(len(pack_list)):
                    if pack_list[i][0] in ['4', '20', '26', '33', '46', 'time']:
                        pass
                    else:
                        f.write(pack_list[i][0] + '的总分是：{}，今日加减分数是：{}，今日加减分数原因是：{}\n'.format(str(class_info[pack_list[i][0]]['总分']), str(class_info[pack_list[i][0]]['加减分数']), str(class_info[pack_list[i][0]]['今日加减分数原因'])))
            showinfo(title='提示', message='导出成功！')

    def search(self, text1, entry1):
        text_temp = text1.get(0.0, END)
        entry_text = entry1.get()
        text = text_temp.split('\n')
        search_list = []
        if entry_text == '':
            pass
        else:
            for i in range(len(text)):
                if entry_text in text[i]:
                    search_list.append(text[i])
        text1.delete(0.0, END)
        for item in search_list:
            text1.insert(END, item + '\n')


class out:
    def __init__(self, master):
        self.master = master
        self.win = Frame(self.master)
        self.win.place(relx=0, rely=0, relwidth=1, relheight=1)

        label1 = Label(self.win, text='导出界面')
        label1.pack()

        button1 = Button(self.win, text='导出', command=self.out)
        button1.pack()

        label2 = Label(self.win, text='返回按钮')
        label2.pack()

        button2 = Button(self.win, text='返回', command=self.back)
        button2.pack()

    def out(self):
        file = asksaveasfilename(title='导出文件', initialdir='C:\\', filetypes=[('txt文本文档', '*.txt'), ('excel（暂时不支持）', '*.xlsx'), ('全部文件', '*.*')], defaultextension='*.txt')

        if file:
            with open(file=file, mode='a+', encoding='utf-8') as f:
                for nums in class_info.keys():
                    if nums == '4':
                        pass
                    elif nums == '20':
                        pass
                    elif nums == '26':
                        pass
                    elif nums == '33':
                        pass
                    elif nums == '46':
                        pass
                    elif nums == 'time':
                        pass
                    else:
                        f.write(str(nums) + '的总分是：{}，今日加减分数是：{}，今日加减分数原因是：{}\n'.format(str(class_info[nums]['总分']), str(class_info[nums]['加减分数']), str(class_info[nums]['今日加减分数原因'])))
            f.close()
        showinfo(title='成功', message='导出成功')

    def back(self):
        self.win.destroy()
        main_window(self.master)


if __name__ == '__main__':
    t = Tk()
    tk(t)
    t.mainloop()