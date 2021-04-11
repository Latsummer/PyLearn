#coding=utf-8
import requests
import json
if __name__ == "__main__":
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

    kw = input("enter 地名: ")
    param = {
        "cname" : "", 
        "pid" : "",
        "keyword" : kw,
        "pageIndex" : "1",
        "pageSize" : "10"
    }

    response = requests.post(url = url, params = param, headers = headers)
    dic_obj = response.json()

    print(dic_obj)