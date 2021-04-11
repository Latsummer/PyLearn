#coding=utf-8
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

if __name__ == "__main__":
    url = "https://www.baidu.com/s?ie=UTF-8&wd=ip"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    page_text = requests.get(url = url, headers = headers)
    page_text.encoding = "utf-8"

    with open("./11.html", "w") as fp:
        fp.write(page_text.text)

    #tree = etree.HTML(page_text.text)

    #ip = tree.xpath("//div[@id = 'tab0_ip']/text()")[0]
    #print(ip)
    #print("hehe呵呵额")