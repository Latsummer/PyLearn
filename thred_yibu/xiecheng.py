import asyncio

async def request(url):
    print("正在请求的是 ", url)
    print("请求完成 ", url)
    return url

#被async修饰的函数，在被调用之后返回一个协程对象
c = request("www.baidu.com")

#创建一个事件循环对象
#loop = asyncio.get_event_loop()

#将协程对象注册到loop中，然后启动事件循环loop
#loop.run_until_complete(c)

#task的使用
#loop = asyncio.get_event_loop()
#tasks = loop.create_task(c)
#print(tasks)

#loop.run_until_complete(tasks)

#print(tasks)

#future的使用
#loop = asyncio.get_event_loop()
#tasks = asyncio.ensure_future(c)
#print(tasks)

#loop.run_until_complete(tasks)
#print(tasks)

def callBack_func(task):
    print(task.result())

#绑定回调
loop = asyncio.get_event_loop()
tasks = asyncio.ensure_future(c)
tasks.add_done_callback(callBack_func)
loop.run_until_complete(tasks)