# 验证码识别
- 反爬机制：识别验证码图片重的数据，用于模拟登陆操作
- 常用操作：第三方自动识别
1. 云打码
2. 超级鹰
3. 极速打码

# 模拟登录
CheckPython2021..

http/https协议特性：无状态
没有请求到对应页面的原因：发起第二次个人主页面的请求时，服务器端不知道此次请求是基于登录状态下的请求的

Cookie：用来让服务器端记录客户端的相关状态
1. 手动处理：通过抓包工具获取cookie值，将该值封装到headers中
2. 自动处理：
    cookie值的来源：
        登录时返回的头部信息中Set-Cookie，由服务端创建的
    session会话对象：
        可以进行请求的发送
        如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中
    session使用：
        创建session对象：session = requests.Session()
        使用session对象进行模拟登陆post请求的发送（cookie会被存储在session中）
        session对象对个人主页界面对应的get请求进行发送（携带cookie）