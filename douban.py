#coding=utf-8
import requests
import json

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"
    param = {
        "type": "17",
        "interval_id": "100:90",
        "action": "", 
        "start": "0",
        "limit": "20"
    }
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

    response = requests.get(url = url, params = param, headers = headers)

    list_data = response.json()

    fp = open("./douban.json", "w", encoding="utf-8")
    json.dump(list_data, fp, ensure_ascii=False)
    print("end")
