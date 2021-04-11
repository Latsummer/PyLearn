#coding=utf-8
import requests
import io
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )

if __name__ == "__main__":
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    url = "https://www.aqistudy.cn/historydata/"
    page_text = requests.get(url = url, headers = headers).text

    tree = etree.HTML(page_text)
    li_list = tree.xpath("//div[@class = 'bottom']/ul/li")

    all_citys = []
    for li in li_list:
        hot_city = li.xpath("./a/text()")[0]
        all_citys.append(hot_city)

    city_names_list = tree.xpath("//div[@class='bottom']/ul/div[2]/li")
    for li in city_names_list:
        city_name = li.xpath("./a/text()")[0]
        all_citys.append(city_name)

    fp = open("./city.txt", 'w')
    for city in all_citys:
        city = city + '\n'
        fp.write(city)