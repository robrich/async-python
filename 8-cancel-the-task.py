import asyncio

async def do_work(sec):
    print(f"start waiting for {sec}")
    await asyncio.sleep(sec) # or any async
    print(f"done waiting for {sec}")

async def main():
    print('launched')
    print('calling do_work')
    try:
        task = asyncio.create_task(do_work(10))
        await asyncio.wait_for(task, timeout=2.0) # seconds
        print('finished waiting')
    except asyncio.TimeoutError as err:
        print('gave up waiting and canceled it')
        task.cancel()
    print('exited do_work')

asyncio.run(main())
