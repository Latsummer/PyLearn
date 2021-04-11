import time
import asyncio
import aiohttp

async def add(a, b):
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
    #time.sleep(1)
    #挡在asyncio中遇到阻塞操作时必须进行手动挂起
    await asyncio.sleep(1)
    #print(a + b)

if __name__ == "__main__":
    start_time = time.time()
    list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 1
    tasks = []
    loop = asyncio.get_event_loop() 
    for i in range(1, 10000):
        task = add(i, num)
        tasks.append(task)

    #需要将任务列表封装到wait中
    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time() - start_time)