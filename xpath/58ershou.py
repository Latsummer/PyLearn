#coding=utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )
from lxml import etree

if __name__ == "__main__":
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    url = "https://xa.58.com/ershoufang/"
    page_text = requests.get(url=url, headers=headers)

    #数据解析
    tree = etree.HTML(page_text.text)
    div_list = tree.xpath("//section[@class='list']/div")

    fp = open('58.txt', 'w')
    for div in div_list:
        titel = div.xpath("./a/div[2]//h3/text()")[0]
        #print(titel)
        fp.write(titel)
        fp.write('\n')