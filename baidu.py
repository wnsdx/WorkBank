#-*-coding:utf-8-*-
import requests

# # coding:utf-8
# from urllib import request
#
# def down(a,b,c):
#     '''
#
#     :param a: 下载次数
#     :param b:  单位下载的大小 单位：字节
#     :param c:  文件的大小
#     :return:
#     '''
#     print('=====a=====')
#     print(a)
#     print('=====b=====')
#     print(b)
#     print('======c====')
#     print(c)
#     d = a*b
#     result = d/c
#     if result >=1:
#         result =1
#     print(result)
# url = 'http://img.zcool.cn/community/0125fd5770dfa50000018c1b486f15.jpg@1280w_1l_2o_100sh.jpg'
# request.urlretrieve(url,'1.jpg',down)


url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=420&rn=30&gsm=1a4&1546787621430='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Referer':'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%9B%BE%E7%89%87&oq=%E5%9B%BE%E7%89%87&rsp=-1'
}
parame = {
    'tn':'resultjson_com',
    'ipn':'rj',
    'ct':'201326592',
    'is':' ',
    'fp':'result',
    'queryWord':'图片',
    'cl':'2',
    'lm':'-1',
    'ie':'utf-8',
    'oe':'utf-8',
    'adpicid':' ',
    'st':'-1',
    'z':' ',
    'ic':'0',
    'hd':' ',
    'latest':' ',
    'copyright':' ',
    'word':'图片',
    's':' ',
    'se':' ',
    'tab':' ',
    'width':' ',
    'height':' ',
    'face':'0',
    'istype':'2',
    'qc':' ',
    'nc':'1',
    'fr':' ',
    'expermode':' ',
    'force':' ',
    'pn':'800',
    'rn':'40',
    'gsm':'1a4',
    '1546787621430':' ',
}
response = requests.get(url = url,headers = headers,params=parame)
content = response.json().get('data')
print(content)
for data in content:
    img_url = data.get('middleURL')
    print(img_url)
print(len(content))
