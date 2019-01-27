# -*- coding:utf-8 -*-
import re
import requests

if __name__ == "__main__":
    url = "https://www.qiushibaike.com/pic/"
    headers = {
        "Referer": "https://www.qiushibaike.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    result = req.content.decode()
    # print(result)
    # <img src="//pic.qiushibaike.com/system/pictures/12108/121089034/medium/SIWRF6JMORIDGNIY.jpg" alt="故事后续">
    imgs = re.findall(r'<img src="(.*?)"', result)
    # print(img)
    for img in imgs:
        print("==================")
        print(img)

    pass