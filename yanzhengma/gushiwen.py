#coding=utf-8
import base64
import json
import requests
from lxml import etree

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

def GetToken():
    url = "http://api.jrdama.com:999/api/login?username=zpfzzl&password=zpfandzzl0106&isup=1"
    prarm = {
        "Content-Type" : "form-data"
    }

    response = requests.get(url = url, headers = headers, params=prarm).json()
    token = response["data"]["token"]

    return token

def GetValue(im, token):
    im = base64.b64encode(im)
    impara = {
        "token": token,
	    "image": im,
        "imageback": "",
	    "type": "1005",
	    "angle": "",
	    "soft": ""
    }
    imurl = "http://api.jrdama.com:999/api/base64"
    response = requests.post(imurl, impara, headers).json()
    if(response["msg"] == "Success"):
        print(response["data"]["result"])
    else:
        print("错误")

if __name__ == "__main__":
    token = GetToken()
    url = "https://www.gswen.cn/mbuser/login.php"
    
    page_text = requests.get(url = url, headers = headers).text
    tree = etree.HTML(page_text)
    
    imsrc = tree.xpath("//img[@id='vdimgck']/@src")[0]
    imsrc = imsrc[2:]
    imsrc = "https://www.gswen.cn" + imsrc

    im = requests.get(url = imsrc, headers = headers).content
    with open("./a.jpg", "wb") as fp:
        fp.write(im)
    
    ret = GetValue(im, token)