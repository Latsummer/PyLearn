# xpath解析原理
1. 实例化一个etree对象，且需要将被解析的页面源码数据加载到该对象中
2. 调用etree对象重的xpath方法结合xpath表达式实现标签的定位和内容的捕获
## 环境
lxml
## 如何实例化一个etree对象
1. 将本地html文档中的源码数据加载到etree对象中：
    `etree.parse(filePath)`
2. 可以将从互联网中获取的源码加载到该对象中
    `etree.HTML("page_text")`
xpath("xpath表达式")
- `/`： 表示从根结点开始定位，表示的是一个层级
        `tree.xpath("/html/body/div")`
- `//`：表示多个层级，可以表示从任意位置开始定位
        `tree.xpath("/html//div)`
        `tree.xpath("//div")`
- 属性定位：`//div[@class='song']`  tag[@attrName="attrValue]
- 索引定位：`//div[@class='song']/p[3]` **索引是从1开始的！**
- 取文本：`//div[@class='tang']//li[5]/a/text()`, 返回值放在列表中
         `//li[7]//text()`
         /text()：获取的是标签中直系文本的内容
         //text()：获取的是非直系文本内容（所有的文本内容）
         `/div[@class='tang']/text()`

- 取属性： `//div[@class='song']/img/@src`
        /@attrName ==> img/src