#coding=utf-8
import requests
import os
import re
from lxml import etree


headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

def enter_src(src_url):
    response = requests.get(url = src_url, headers = headers)
    response.encoding = "utf-8"
    page_text = response.text
    tree = etree.HTML(page_text)

    title = tree.xpath("//div[@class='ppt_tit clearfix']/h1/text()")[0] + ".rar"
    title = title.replace(" ", "")
    down_url = (tree.xpath("//ul[@class='clearfix']/li")[0]).xpath("./a/@href")[0]
    down_url = down_url.replace(" ", "")
    
    down = requests.get(url=down_url, headers=headers).content
    path = "./jianli/" + title
    with open(path, "wb") as fp:
        fp.write(down)
        print(title, "ok ")
 

if __name__ == "__main__":
    if not os.path.exists("./jianli"):
        os.mkdir("./jianli")
    for i in range(3, 11):
        if(i == 1):
            url = "https://sc.chinaz.com/jianli/free.html"
        else:
            url = "https://sc.chinaz.com/jianli/free_%d.html"
            url = format(url%i)

        page_text = requests.get(url = url, headers = headers).text
        
        tree = etree.HTML(page_text)
        div_list = tree.xpath("//div[@id='main']/div/div")

        for div in div_list:
            src = div.xpath("./a/@href")[0]
            src = "https:" + src
            enter_src(src)

