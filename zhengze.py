#coding=utf-8
import requests

if __name__ == "__main__":
    url = "https://pic.qiushibaike.com/system/pictures/12417/124171088/medium/Y8ML9VQBX630CEDI.jpg"
    #content返回二进制图片数据
    #text返回字符串形式
    #json返回对象类型
    img_data = requests.get(url = url).content

    with open("./tu.jpg", "wb") as fp:
        fp.write(img_data)