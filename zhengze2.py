#coding=utf-8
import requests
import re
import os

if __name__ == "__main__":

    if not os.path.exists("./qiutuLibs"):
        os.mkdir("./qiutuLibs")

    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    url = "https://www.qiushibaike.com/imgrank/"

    page_text = requests.get(url = url, headers = headers).text
    
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)

    for src in img_src_list:
        src = 'https:' + src
        img = requests.get(url = src, headers = headers).content
        img_name = src.split('/')[-1]
        imgPath = "./qiutuLibs/" + img_name
        imgPath = "./qiutuLibs/" + img_name
        with open(imgPath, "wb") as fp:
            fp.write(img)
            print(img_name, " OK")