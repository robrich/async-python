import asyncio

async def do_work(sec):
    print(f"start waiting for {sec}")
    await asyncio.sleep(sec) # or any async
    print(f"done waiting for {sec}")
    return sec

async def main():
    print('launched')

    print('starting and awaiting both')
    [res2, res1] = await asyncio.gather(do_work(2), do_work(1))
    print('finished')
    print(f"res2: {res2}, res1: {res1}")

asyncio.run(main())
