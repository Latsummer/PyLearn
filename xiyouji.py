#coding=utf-8
import requests
import lxml
from bs4 import BeautifulSoup
if __name__ == "__main__":
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    url = "https://www.shicimingju.com/book/xiyouji.html"
    page_text = requests.get(url = url, headers = headers).text

    #解析page_text

    #1. 实例化一个BeautifulSoup对象，将页面源码数据加载到对象当中
    soup = BeautifulSoup(page_text, features = 'lxml')
    li_list = soup.select(".book-mulu > ul > li")
    fp = open("./xiyouji.txt", "w", encoding="utf-8")
    for li in li_list:
        title = li.a.sting
        detail_url = "https://www.shicimingju.com" + li.a["href"]
        detail_page_text = requests.get(url = detail_url, headers = headers).text
        detail_soup = BeautifulSoup(detail_page_text, features = 'lxml')
        div_tag = detail_soup.find("div", class_ = "chapter_cotent")
        content = div_tag.text
        fp.write(title + ": " + content + "\n\n\n\n\n\n")
        print(title , "OK ")
