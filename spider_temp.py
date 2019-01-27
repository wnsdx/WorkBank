# -*- coding:utf-8 -*-
try:
    import urllib2 as request  #Python2导入
except:
    from urllib import request#Python3导入

url="https://www.qiushibaike.com/"
headers = {
    'Rederer':'https://www.qiushibaike.com/pic/',#请求来源
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/63.0'#请求身份
}


if __name__ == "__main__":
    # 构建一个请求
    req = request.Request(url, headers=headers)
    # 发送请求
    response = request.urlopen(req)
    # 读取返回内容
    result = response.read().decode()
    # 输出
    print(result)
    pass