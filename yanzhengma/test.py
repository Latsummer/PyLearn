#coding = utf-8
import requests
import json
import base64

if __name__ == "__main__":
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    url = "http://api.jrdama.com:999/api/login?username=zpfzzl&password=zpfandzzl0106&isup=1"
    prarm = {
        "Content-Type" : "form-data"
    }

    response = requests.get(url = url, headers = headers, params=prarm).json()
    token = response["data"]["token"]
    print(token)
    im = open("./a.jpg", "rb").read()
    im = base64.b64encode(im)

    impara = {
        "token": token,
	    "image": im,
        "imageback": "",
	    "type": "1001",
	    "angle": "",
	    "soft": ""
    }
    imurl = "http://api.jrdama.com:999/api/base64"

    imreques = requests.post(imurl, impara, headers)

    print(imreques.json())