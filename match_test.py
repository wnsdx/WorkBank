# -*- coding:utf-8 -*-
import re

if __name__ == "__main__":

    print("==============组匹配==================")
    str = "hello world"
    res = re.findall('\wo', str)  # 匹配一个数字或者字母或者下划线后面再加o字母
    print(res)
    res = re.findall('\w(o)', str)  # 匹配前面有一个数字或者字母或者下划线的o字母
    print(res)

    print("=============反贪婪匹配===============")
    str = "<img aaaaabbb><cccc>"
    res = re.findall(r'<img (.*?)><(.*?)>', str)  # <img 任意元素一次，以第一个>结尾
    print(res)

    print("=============贪婪匹配===============")
    res = re.findall(r'<img (.*>)', str)  # <img 任意元素一次，以最后一个>结尾
    print(res)

    pass