#coding=utf-8
import requests
import json

if __name__ == "__main__":
    post_url = "https://fanyi.baidu.com/sug"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

    while True:
        word = input("enter a word(enter 'abc' for break): ")
        if word == "abc":
            break
        data = {
            "kw" : word
        }

        response = requests.post(post_url, data, headers)

        #json方法返回一个对象，需要响应数据是json类型,返回的是字典类型
        dic_obj = response.json()

        for i in dic_obj["data"]:
            print("英: ", i["k"], "\t汉: ", i["v"])
        #fp = open("./dog.json", "w", encoding="utf-8")
        #json.dump(dic_obj, fp, ensure_ascii=False)

    print("end")