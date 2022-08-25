#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   coding2file.py
@Time    :   2022/08/25 07:44:19
@Author  :   Ayatale 
@Version :   1.1
@Contact :   ayatale@qq.com
@Github  :   https://github.com/brx86/
@Desc    :   None
"""
from rich import print
from rich.traceback import install

install()


import re, shutil, sys

file_name = sys.argv[1]
with open(file_name) as f:
    raw_text = f.read()

pattern = re.compile(r"https://ayatale.*.png")
pic_list: list[str] = pattern.findall(raw_text)

for n, pic_url in enumerate(pic_list):
    pic_name_old = pic_url.split("/")[-1]
    pic_name_new = f'{file_name.split("-")[0]}.{n+1}.png'
    print(f"{pic_name_old} -> {pic_name_new}")
    shutil.copyfile(f"file/{pic_name_old}", f"pic/{pic_name_new}")
    raw_text = raw_text.replace(pic_url, f"/pic/{pic_name_new}")


with open(file_name, "w") as f:
    f.write(raw_text)
