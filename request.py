#coding=utf-8
import requests
#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )

if __name__ == "__main__":
    url = "https://zhaozhuolin.com/"
    response = requests.get(url)
    page_text = response.text
    #print(page_text)

    with open("./zzl.html", 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print("end!")
