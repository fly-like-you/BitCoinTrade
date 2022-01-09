import asyncio
import multiprocessing as mp
import time
import websockets
import json


async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri, ping_interval = None) as websocket:
        greeting = await websocket.recv()
        print(greeting)

        subscribe_fmt = {
            "type" : "ticker",
            "symbols": ["BTC_KRW"],
            "tickTypes": ["1H"]
        }

        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)
async def main():
    await bithumb_ws_client()
asyncio.run(main())
# def worker():
#     proc = mp.current_process()
#     print(proc.name)
#     print(proc.pid)
#     time.sleep(5)
#     print("Subprocess End")
#
# if __name__ == "__main__":
#     #main process
#     proc = mp.current_process()
#     print(proc.name)
#     print(proc.pid)
#     #process spawning
#     p = mp.Process(name = "SubProcess", target = worker)
#     p.start()
#
#     print("MainProcess End")
# async키워드가 있는 함수를 코루틴이라고 부름 호출방법도 다름 이벤트루프가 필요함
# async def async_func1():
#     print("hello")
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(async_func1())
# loop.close
# #asyncio.run(async_func1())
# 비동기와 동기 함수
# async def make_americano():
#     print("아메리카노 주문 접수")
#     await asyncio.sleep(3)
#     print("아메리카노 나왔습니다")
#     return "아메리카노"
#
# async def make_latte():
#     print("라떼 주문 접수")
#     await asyncio.sleep(5)
#     print("라떼 나왔습니다")
#     return "라떼"
#
# async def main():
#     coro1 = make_americano()
#     coro2 = make_latte()
#     result = await asyncio.gather(
#         coro1,
#         coro2
#     )
#     print(result)
#
# print("Main Start")
# asyncio.run(main())
# print("Main End")