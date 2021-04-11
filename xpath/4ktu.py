#coding=utf-8
import requests
import os
import re
from lxml import etree

if __name__ == "__main__":

    if not os.path.exists("./4K"):
        os.mkdir("./4K")

    url = "https://pic.netbian.com/4kmeinv/"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

    response = requests.get(url = url, headers = headers)
    #可以手动设定响应数据的编码格式
    #response.encoding = "utf-8"
    page_text = response.text

    tree = etree.HTML(page_text)

    li_list = tree.xpath("//div[@class='slist']/ul/li")
    for li in li_list:
        img_url = "https://pic.netbian.com/" + li.xpath("./a/img/@src")[0]
        title = li.xpath("./a/img/@alt")[0] + ".jpg"

        #中文乱码通用解决方案
        title = title.encode("iso-8859-1").decode("gbk")

        img = requests.get(url = img_url, headers = headers).content
        img_path = "./4K/" + title
        with open(img_path, "wb") as fp:
            fp.write(img)
            print(title, " OK")