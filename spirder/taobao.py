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
    u.addheader('Cookie',
                'x=__ll%3D-1%26_ato%3D0; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; l=Al1da54CRNlKwHobvO/Q-QXT7TdWepHr; tracknick=%5Cu94F6%5Cu6CF0%5Cu5F00%5Cu53D1%5Cu8005; t=464361a007c8463db07188b4d22a33e7; cookie2=15db57c7d8d2bf79c38c164f42411869; _tb_token_=8636c9e5b3de; cna=m6IGDtnCTBgCAdznFoIze/w0; pnm_cku822=112UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVAe097Q3lGfCo%3D%7CU2xMHDJ7G2AHYg8hAS8WLgAgDlIzVTleIFp0InQ%3D%7CVGhXd1llXWBZYldsWGxUblFrXGFDd09xTXVKcU5yTHhCeEF0T2E3%7CVWldfS0RMQU7BiYaJAQqFTUKL3kpTHNXfAReJwlfCQ%3D%3D%7CVmhIGCUFOBgkEC0TMwg0CjcXKx8gHT0BPAk0FCgcIx4%2BAj8GO207%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D; res=scroll%3A1903*6130-client%3A1903*601-offset%3A1903*6130-screen%3A1920*1080; cq=ccp%3D1; isg=AsjIpxk4BUQNWGf6ulpvbZJUmTbQUQ1PkR4zwoJ5FMM2XWjHKoH8C15foQDU')
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
        "https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.4c6378107v13kS&brand=26944618&q=westory&sort=s&style=g&industryCatId=all&type=pc#J_Filter",
        "https://list.tmall.com/search_product.htm?q=MISS+SIXTY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=MANDARINA+DUCK&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=UGG&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B6%E0%D7%CB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Armani+Jeans&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=JUICY+COUTURE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=OTT&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B8%E8%C1%A6%CB%BC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%E7%E6%C4%E1%B5%D9%CB%BC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=KAKO&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?cat=50025135&q=%D3%E6&sort=s&style=g&from=sn_1_cat-qp&spm=a220m.1000858.a2227oh.d100#J_crumbs",
        "https://list.tmall.com/search_product.htm?q=%D1%D4%B2%E8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B6%F7%C9%D1&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B8%E8%D6%D0%B8%E8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C3%D7%DC%E7%B6%FB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=OFIMAN&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CF%A3%C9%AB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=ICICLE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=HPLY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D2%FC%C4%AC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%B3%DC%BD%B0%AC%B5%CF%B6%F9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C7%C7%C4%C8%B0%B2%B4%EF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BE%C1%D7%CB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=liaa+lancy&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B7%C6%D7%CB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C2%FC%C4%DD%B7%D2&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Comfit&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%B2%C0%F2%B7%BC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=LA+CLOVER&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D2%C1%CE%AC%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C8%F8%C2%B6%CC%D8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=LIZACHENG&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BB%AA%B8%E8%B6%FB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C9%A3%B7%F6%C0%BC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B5%CF%C9%A3%C4%C8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%C5%B5%D9%C4%C8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CA%AB%C6%AA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D3%F6%BC%FB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=COCOON&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CE%D2%B0%AE%C2%B6%C2%B6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=XG&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B1%F5%B2%A8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%EC%B3%C4%C8%B3%BF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B5%CF%C8%FC%C4%E1%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=ZUKKAPRO&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C9%BD%BB%A8%B2%D3&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C3%D7%E1%B6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D3%F4%CF%E3%B7%C6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=MO%26Co.+edition&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=FRAY+I.D&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Steve%26Vivian&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=BNX&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=snidel&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=ODBO&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B4%EF%D2%C2%D1%D2&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CF%C4%CD%DE%B5%C4%D3%D5%BB%F3&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B5%D8%CB%D8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C4%A6%B0%B2%E7%E6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=PRICH&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%CA%CE%C4%CB%B9%CD%A1&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C6%AE%C0%D9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C6%AE%C0%D9&type=p&cat=all",
        "https://list.tmall.com/search_product.htm?q=%BC%BE%BA%F2%B7%E7&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Roem&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C8%FD%B2%CA.%C0%F6%D1%A9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=NICECLAUP&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%AE%C3%C0%C0%F6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%BC%D7%BF%C0%F6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Body+POPS&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BD%AD%C4%CF%B2%BC%D2%C2&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Loftshine&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=G2000&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B7%C9%C4%F1%BA%CD%D0%C2%BE%C6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=LALABOBO&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=I+LOVE+CHOC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CA%AB%B7%B2%C0%E8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=d%27zzit&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=lily&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=ONE+MORE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Jessy+line&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BF%A8%B1%B4%C4%CE%B6%FB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BA%EC%D0%E4&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=CRZ&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B8%E8%C0%F2%E6%AB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?cat=50025135&q=E+LAND&sort=s&style=g&from=sn_1_cat-qp&spm=a220m.1000858.a2227oh.d100#J_crumbs",
        "https://list.tmall.com/search_product.htm?q=%DA%E6%D6%AF%CE%DD&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=SENSU&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=JACK+JONES&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Yatlas&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=GXG&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Trendiano&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=gxg.jeans&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Teenie+Weenie&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Cabbeen&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CB%D9%D0%B4&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=PLORY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CC%AB%C6%BD%C4%F1&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BC%E1%B3%D6%CE%D2%B5%C4&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%EE%CE%AC%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Lee+Cooper&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BB%DD%C3%C0%CA%D9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Lee&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=MLB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?cat=50025174&brand=3390753&q=MLB&sort=s&style=g&from=sn_1_cat-qp#J_crumbs",
        "https://list.tmall.com/search_product.htm?q=%B1%EB%C2%ED&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=NIKE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Hi+Panda&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=BOY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=inxx&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=CAT&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=NIKE+SP&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=SKECHERS&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=FILA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%A2%B5%CF%B4%EF%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=adidas+neo&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=NEW+BALANCE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BF%EF%CD%FE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%AE%CA%C0%BF%CB%CB%BD&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=REEBOK&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=PONY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=LACOSTE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%D9%C0%F6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D5%E6%C3%C0%CA%AB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C6%E4%C0%D6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CB%FB%CB%FD&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CC%EC%C3%C0%D2%E2&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=BATA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=NINE+WEST&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Stella+Luna&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=ASH&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=WESTORY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B5%CF%DC%BD%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C7%A7%B0%D9%B6%C8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=ST%26SAT&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C5%B5%B1%B4%B4%EF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?brand=29837721&q=AS&sort=s&style=g&from=sn_1_brand-qp&spm=a220m.1000858.a2227oh.d100#J_crumbs",
        "https://list.tmall.com/search_product.htm?q=%D1%C5%CA%CF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B9%FE%C9%AD&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=FED&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C1%B5%C9%D0%C2%DC%C9%AF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CB%BC%BC%D3%CD%BC&type=p&cat=all",
        "https://list.tmall.com/search_product.htm?q=%C0%B3%B6%FB%CB%B9%B5%A4&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%F5%DE%E3%BA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C3%EE%C0%F6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BE%C1%D7%CB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=DUNNU&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=FINITY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D2%D7%B7%C6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=MORELINE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B8%E8%C1%A6%CB%BC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Teenie+Weenie&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D0%A1%D6%ED%B0%E0%C4%C9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%A2%C2%F5%B5%D9%C4%E1&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B5%CF%B5%CF%C2%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=CAMKIDS&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Mini+Peace&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D0%A1%D0%A6%C5%A3&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%D6%B1%C8%D3%C6%D3%C6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D0%C1%B0%CD%C4%C8%C4%C8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=AIMER+KIDS&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D3%A2%CA%CF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CA%AE%D4%C2%C2%E8%DF%E4&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B1%BE%C9%AB%C3%DE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%F6%D3%A4%B7%BF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%AD%B1%C8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=allo%26lugh&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C2%ED%C0%AD%B6%A1&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=U.JAR&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=jnby+by+JNBY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BF%C9%B0%AE%D0%E3&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=gxg+kids&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CC%A9%C0%BC%C4%E1%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%CD%B1%B4&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D2%C0%CE%C4&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CD%FE%CB%B9%BF%B5%C4%E1&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C2%FB%B9%FE%B6%D9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D3%A2%B9%FA%B1%A3%C2%DE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D1%C5%B8%EA%B6%FB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B1%A4%C4%E1&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C6%E4%C0%D6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=ELLE+HOMME&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C9%AD%B4%EF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=BYFORD&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BE%C5%C4%C1%CD%F5&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B5%C2%F6%E8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=LACOSTE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B1%F5%B2%A8&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=G2000&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=INTREX&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=JAMES+KINGDOM&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%AE%C4%BD%CF%C8%C9%FA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=IVU&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D1%C5%B8%EA%B6%FB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%AD%B0%D8%BC%D2%D1%C5&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D7%F4%B5%A4%C5%AB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=CAT&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?cat=50020894&q=%BA%C9%C2%ED&sort=s&style=g&from=sn_1_cat-qp&spm=a220m.1000858.a2227oh.d100#J_crumbs",
        "https://list.tmall.com/search_product.htm?cat=50020909&q=%BA%C9%C2%ED&sort=s&style=g&from=sn_1_cat-qp&spm=a220m.1000858.a2227oh.d100#J_crumbs",
        "https://list.tmall.com/search_product.htm?q=Columbia&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=THE+NORTH+FACE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=LOWA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CC%BD%C2%B7%D5%DF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=JackWolfskin&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C5%B5%CA%AB%C0%BC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%EE%C4%FE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D6%DE%BF%CB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B4%E5%C9%CF%B4%BA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=it+MICHAA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B8%E7%CE%C4%BB%A8%D4%B0&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=SELECTED&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B8%BB%C2%DE%C3%D4&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=DISNEY&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BB%F9%C5%B5%C6%D6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B1%C8%BB%AA%C0%FB%B1%A3%C2%DE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BE%C5%C4%C1%CD%F5&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C9%BC%C9%BC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CA%A5%B4%F3%B1%A3%C2%DE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B6%F5%B6%FB%B6%E0%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=JEEP&type=p&cat=all",
        "https://list.tmall.com/search_product.htm?q=%B9%FE%BC%AA%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=Mind+Bridge&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=NAUTICA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=MARK+FAIRWHALE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=FORTEI&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?cat=50025174&q=%C2%B9%CD%F5&sort=s&style=g&from=sn_1_cat-qp&spm=a220m.1000858.a2227oh.d100#J_crumbs",
        "https://list.tmall.com/search_product.htm?q=%B1%A8%CF%B2%C4%F1&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=J.BASCHI.&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CA%E6%D1%C5&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=SWISSWIN&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%CF%B2%C2%EA%B6%FB%CD%BC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=BLACKYAK&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B0%AE%B2%BD&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%B5%D9%CB%B9%B8%A5&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%D2%C2%CF%E3%C0%F6%D3%B0&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%BF%A8%B1%B4%C4%CE%B6%FB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C5%B7%CA%B1%C1%A6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "https://list.tmall.com/search_product.htm?q=%C0%EE%BA%EC%B9%FA%BC%CA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
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
