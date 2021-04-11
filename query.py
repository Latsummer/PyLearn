#coding=utf-8
import requests

if __name__ == "__main__":

    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

    url = "https://www.sogou.com/web"

    kw = input("enter a word: ")
    param = {
        "query" : kw
    }

    response = requests.get(url = url, params = param, headers = headers)
    page_text = response.text

    fileName = kw + ".html"
    with open(fileName, "w", encoding="utf-8") as fp:
        fp.write(page_text)
    
    print("ok")