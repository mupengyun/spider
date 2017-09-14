# coding=utf-8

import urllib
from bs4 import BeautifulSoup
import os

savepath = r"/Users/mupengyun/img"

def mkdir(path):
    if os.path.exists(path):
        return
    os.mkdir(path)

def getImg(url):
    u = urllib.URLopener()
    u.addheaders = []
    u.addheader('User-Agent',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    u.addheader('Cookie','')
    html = u.open(url)
    print (html.headers)
    bs = BeautifulSoup(html.read().decode('gbk'), "html.parser")
    #  总页数
    sourceUrls = [url]
    totalPage = int(bs.find("input", {"name": "totalPage"}).get("value"))
    for i in range(1, totalPage - 1):
        soureUrl = url.replace('q=', 's=' + str(i * 60) + '&q=')
        sourceUrls.append(soureUrl)
    # 每页图片
    for soureUrl in sourceUrls:
        try:
            html = u.open(soureUrl)
            bs = BeautifulSoup(html.read().decode('gbk'), "html.parser")
            items = bs.findAll("div", {"class": "product"})
            for item in items:
                # 天猫类目ID
                categoryId = item.get("data-atp").split(",")[2]
                imgUrl = item.a.img.attrs.values()[0]
                savefilename = os.path.join(savepath, categoryId)
                mkdir(savefilename)
                u.retrieve('https:' + str(imgUrl), os.path.join(savefilename, imgUrl.split("/")[-1]))
        except IOError as e:
            print (e.message)
        continue

    u.close()

if __name__ == "__main__":
    mkdir(savepath)
    urls = [
        "https://list.tmall.com/search_product.htm?brand=3713796&q=MCM&sort=s&style=g&from=mallfp..pc_1_searchbutton&spm=875.7931836/B.a2227oh.d100&type=pc",
        ]
    log = open(savepath+"/log.txt","w")
if __name__ == '__main__' :
    for url in urls:
        print ("开始爬取url" + url)
        log.writelines("开始爬取url" + url)
        getImg(url)
        print ("结束爬取url" + url)
        log.writelines("结束爬取url" + url)
    log.close()
    print ("全部爬取结束")
