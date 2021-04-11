import requests
import asyncio
import aiohttp
import os
from lxml import html

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

async def download_img(img_src, img_path):
    img_name = img_src[-7:]
    #print(img_path)
    if os.path.exists(img_path):
        return
    async with aiohttp.ClientSession() as session:
        async with await session.get(url = img_src, headers = headers) as response:
            #text()返回字符串形式的响应数据
            #read()返回二进制形式的数据
            #json()返回json对象
            img = await response.read()
            fp = await open(img_path, "wb")
            await fp.write(img)


if __name__ == "__main__":
    url = "https://l528avmyo67mic8u.com/home/piclist/7/830-1.html"

    response = requests.get(url=url, headers = headers, verify=True)
    response.encoding = "utf-8"

    etree = html.etree

    tree = etree.HTML(response.text)
    img_src_list = tree.xpath("//div[@class='listpic']/a/@href")

    tasks = []

    for img_src in img_src_list:

        img_src = "https://l528avmyo67mic8u.com" + img_src
        img_page_response = requests.get(url = img_src, headers = headers, verify=True)
        img_page_response.encoding = "utf-8"

        img_tree = etree.HTML(img_page_response.text)
        title = img_tree.xpath("//div[@class='title']/h1/text()")

        img_title = title[2][3:]
        floder = "/Users/morgan/PyLearn/Pachong/thred_yibu/Tu/" + img_title
        if not os.path.exists(floder):
            os.mkdir(floder)
        
        list_imgs = img_tree.xpath("//div[@class='nbodys']/p/img/@src")
        for src_img in list_imgs:
            photo_name = img_src[-8:-5] + ".jpg"
            photo_path = floder + "/" + photo_name
            c = download_img(src_img, photo_path)
            task = asyncio.ensure_future(c)
            tasks.append(task)
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
            #if os.path.exists(photo_path):
            #    print("is here 嗷嗷")
            #    continue
            #try:
            #    photo = requests.get(url = src_img, headers = headers, verify=True, timeout = (3, 5)).content
            #except requests.exceptions.ReadTimeout:
            #    continue
            #except requests.exceptions.ConnectionError:
            #    continue
            
            #with open(photo_path, "wb") as ph:
            #    ph.write(photo)
            #    print(photo_path, " ok!")

    #page_text = response.text
    #with open("./indxe.html", "w") as fp:
    #    fp.write(page_text)