# -*- coding:utf-8 -*-
import json
import tkinter
from tkinter import messagebox
"""
author: CHT(D BOY; 成昊天)
E-mail: dboycht@qq.com
Welcome to visit my gitee or github!
gitee: gitee.com/sky-eye
github: github.com/chenghaotian
Environment: python 3.9.0
"""

w = tkinter.Tk()
w.title("Cheq-foreign-pu V0.12")
w.geometry("330x130")
lj = open("./languages_json.json", encoding="utf-8")
lj = json.load(lj)
lj = dict(lj)
version = lj["Version"]

with open("./language.txt", encoding="utf-8") as l_d:
    v_grammar = l_d.readline()[-5:-1]
    if v_grammar.strip() != version[0].strip():
        messagebox.showwarning("Warning", "Version error, please download the corresponding version plug-in")
        exit()
    else:
        pass
f_will_change = open("./language.txt", "w", encoding="utf-8")
with open("./languages.txt", encoding="utf-8") as langs:
    l_list = langs.readlines()


def c_c_s():
    for ccs in l_list[lj["简体中文"][0]: lj["简体中文"][1]+1]:
        f_will_change.write(ccs)
    f_will_change.close()
    exit(0)


def c_j():
    for ccs in l_list[lj["日本語"][0]: lj["日本語"][1]+1]:
        f_will_change.write(ccs)
    f_will_change.close()
    exit(0)


def c_r():
    for ccs in l_list[lj["русский язык"][0]: lj["русский язык"][1]+1]:
        f_will_change.write(ccs)
    f_will_change.close()
    exit(0)


def c_e():
    for ccs in l_list[lj["English"][0]: lj["English"][1]+1]:
        f_will_change.write(ccs)
    f_will_change.close()
    exit(0)


def c_c_t():
    for ccs in l_list[lj["繁體中文"][0]: lj["繁體中文"][1]+1]:
        f_will_change.write(ccs)
    f_will_change.close()
    exit(0)


def c_c_o():
    for ccs in l_list[lj["文言文"][0]: lj["文言文"][1]+1]:
        f_will_change.write(ccs)
    f_will_change.close()
    exit(0)


if __name__ == '__main__':
    b_ccs = tkinter.Button(w, text='简体中文', command=c_c_s)
    b_cj = tkinter.Button(w, text='日本語', command=c_j)
    b_cr = tkinter.Button(w, text='русский язык', command=c_r)
    b_ce = tkinter.Button(w, text='English', command=c_e)
    b_ct = tkinter.Button(w, text='繁體中文', command=c_c_t)
    b_co = tkinter.Button(w, text='文言文', command=c_c_o)
    b_ccs.place(x=20, y=20)
    b_cj.place(x=120, y=20)
    b_cr.place(x=220, y=20)
    b_ce.place(x=20, y=80)
    b_ct.place(x=120, y=80)
    b_co.place(x=220, y=80)
    w.mainloop()
