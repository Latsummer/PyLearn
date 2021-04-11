#coding=utf-8
import base64
import json
import requests
from hashlib import md5
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

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
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    url = "http://www.renren.com/SysHome.do"
    chaojiying = Chaojiying_Client('zpfzzl', 'zpfandzzl0106', '914512')

    response = requests.get(url = url, headers = headers)
    tree = etree.HTML(response.text)
    img_src = tree.xpath("//img[@id='verifyPic_login']/@src")[0]

    img = requests.get(url = img_src, headers = headers).content
    with open("./renren.jpg", "wb") as fp:
        fp.write(img)
    
    ret = chaojiying.PostPic(img, 5000)["pic_str"]
    ret = ret.upper()
    print(ret)

    data = {
        "email": "18066704330",
        "icode": ret,
        "origURL": "http://www.renren.com/home",
        "domain": "renren.com",
        "key_id": "1",
        "captcha_type": "web_login",
        "password": "69961487985700bd8a8a5b5fc73b8a4125e67e126b81b304e24a3690a773eb34",
        "rkey": "4f94f2d55a49bb9971cb548e5e6a505c",
        "f": "http%3A%2F%2Fwww.renren.com%2F976484947"
    }

    login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021201147528"
    login_text = requests.post(url = login_url, data = data, headers = headers).text
    with open("./renren.html", "w") as fp:
        fp.write(login_text)
