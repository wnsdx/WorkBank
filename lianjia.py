# -*- coding:utf-8 -*-
from urllib import request
import os
from datetime import datetime

if __name__ == "__main__":

    # type = input('买二手房还是租房>>>')
    type ='zufang'
    types = ['zufang', 'ershoufang']
    if type in types:
        page=3
        # page = input('输入查看的页码>>>')
        if page == 1:
            Referer = 'https://sz.lianjia.com/'
        else:
            Referer = 'https://bj.lianjia.com/%s/pg%s/' % (type, int(page) - 1)
            url = 'https://sz.lianjia.com/%s/pg%s/' % (type, page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Referer': Referer
    }
    # 构建一个请求
    req = request.Request(url, headers=headers)
    # 发送请求
    response = request.urlopen(req)
    # 读取返回内容
    result = response.read().decode()
    # 输出
    print(result)
    Now_time=datetime.now().strftime('%Y-%m-%d')
    # print(type(Now_time))
    with open(r'text%s.txt'%(Now_time),'a') as note:
        now_time_detail=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note.write('\n=====================%s========================\n'%(now_time_detail))
        note.write(result)
        pass
    pass