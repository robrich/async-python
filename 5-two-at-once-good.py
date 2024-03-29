import asyncio

async def do_work(sec):
    print(f"start waiting for {sec}")
    await asyncio.sleep(sec) # or any async
    print(f"done waiting for {sec}")
    return sec

async def main():
    print('launched')
    print('calling wait for 2 seconds')
    task2 = asyncio.create_task(do_work(2))
    print('exited wait for 2 seconds')

    print('calling wait for 1 second')
    task1 = asyncio.create_task(do_work(1))
    print('exited wait for 1 second')

    print('awaiting both')
    res2 = await task2
    res1 = await task1

    print('finished')
    print(f"res2: {res2}, res1: {res1}")

asyncio.run(main())
