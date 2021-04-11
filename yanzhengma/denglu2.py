#coding=utf-8
import base64
import json
import requests
from hashlib import md5
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

My_headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

if __name__ == "__main__":
    chaojiying = Chaojiying_Client('zpfzzl', 'zpfandzzl0106', '914512')

    url = "https://www.gswen.cn/mbuser/login.php"
    
    page_text = requests.get(url = url, headers = My_headers).text
    tree = etree.HTML(page_text)

    print("Tree build!")
    
    imsrc = tree.xpath("//img[@id='vdimgck']/@src")[0]
    imsrc = imsrc[2:]
    imsrc = "https://www.gswen.cn" + imsrc

    im = requests.get(url = imsrc, headers = My_headers).content
    with open("./a.jpg", "wb") as fp:
        fp.write(im)
    
    ret = chaojiying.PostPic(im, 6001)["pic_str"]
    print(ret)

    login_param = {
        "fmdo": "login",
        "dopost": "login",
        "gourl": "",
        "userid": "zpfzzl",
        "pwd": "CheckPython2021..",
        "vdcode": ret,
        "keeptime": "86400"
    }
    login_url = "https://www.gswen.cn/mbuser/index_do.php"
    My_headers2 = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "content-type" : "application/x-www-form-urlencoded",
        "cookie": "UM_distinctid=178727a9238453-04703134b41f34-6518217c-13c680-178727a9239381; CNZZDATA1279753275=309515508-1616828006-https%253A%252F%252Fwww.baidu.com%252F%7C1616828006; Hm_lvt_9bdb760c9ebf85ee63897084b01f3ef8=1616828342; Hm_lvt_c99d3afe5f2e1146eb4a7fe26d90dd10=1616828365; PHPSESSID=oumb1tgtchoo1g6hnq7irbuiu7"
    }
    login_res = requests.post(url = login_url,data = login_param, headers = My_headers2).text
    with open("./login.html", "w") as fp:
        fp.write(login_res)