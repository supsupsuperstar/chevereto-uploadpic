# -*- coding: UTF-8 -*-
import tkinter as tk
import glob,os,requests
from tkinter import filedialog
from os import listdir
import base64

def img_base64(path):
    f = open(path, 'rb')
    ls_f = base64.b64encode(f.read())
    f.close()
    return (ls_f)

#chevereto 官方api文档 https://v3-docs.chevereto.com/API/V1.html#api-key

def upload(path):
    img=img_base64(path)    #图像转换成base64

    data = {
        "source": img,
        "url": 'http://starry2020.f3322.net:1212/api/1/upload',     #请求URL
        "action": "upload",
        "key": "b8bcf10c551f29bde6e816cc8c3ecfe6",  #API v1 的密钥
        "format":'json' #设置返回格式 [value：json(默认值)，redirect，txt]
    }
    res = requests.post(data['url'], data=data).json()

    if res is not None:
        if res['status_code'] == 200:
            imgurl = res['image']['url']
        else:
            imgurl = '图片上传失败：' + res['error']['message']
    else:
        print('request失败！')
    return (imgurl)

#打开文件夹
root = tk.Tk()
root.withdraw()
namelist=[]
urllist=''
print('选择要上传的文件夹')
folderpath = filedialog.askdirectory()  # 获得选择好的文件夹
allfilename = listdir(folderpath)  # 所选文件夹下所有的文件名
print('所选文件夹路径:', folderpath)
if folderpath is not None:
    if allfilename == []:
        print('文件夹下没有图片')
    else:
        
        for name in glob.glob(folderpath + '/*.jpg'):
            namelist.append(name[name.index('\\') + 1:] + '\n')
            urllist = upload(name)
            namelist.append(urllist + '\n')

        for name in glob.glob(folderpath + '/*.jpeg'):
                namelist.append(name[name.index('\\') + 1:] + '\n')
                urllist = upload(name)
                namelist.append(urllist + '\n')

        for name in glob.glob(folderpath + '/*.png'):
                    namelist.append(name[name.index('\\') + 1:] + '\n')
                    urllist = upload(name)
                    namelist.append(urllist + '\n')

        for name in glob.glob(folderpath + '/*.gif'):
                        namelist.append(name[name.index('\\') + 1:] + '\n')
                        urllist = upload(name)
                        namelist.append(urllist + '\n')

    f = open(folderpath + '/url.txt', 'w')  #返回的url输出到目录下的url.txt
    for result in namelist:
        f.write(result)

    f.close()
    print('上传完毕!')


