import requests
from lxml import etree

if __name__ == "__main__":
    url = "https://www.buxiuse.com/?cid=7"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    session = requests.Session()
    response = session.get(url = url, headers = headers)
    response.encoding = "utf-8"
    tree = etree.HTML(response.text)

    list_src = tree.xpath("//li[@class = 'span3']//a/@href")
    imgs = []
    for src in list_src:
        res = session.get(url = url, headers = headers)
        res.encoding = "utf-8"
        path = "./buxiuse/" + src[-6:] + ".html"
        with open(path, "w") as fp:
            fp.write(res.text)
        #res_tree = etree.HTML(res.text)
        #img_name = res_tree.xpath("//div[@class='media-body']/h1/text()")
        #img_srcs = res_tree.xpath("//div[@class='image-container image-float-center']//img/@src")    
        #print(img_srcs)