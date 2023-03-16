import asyncio

async def do_work(sec):
    print(f"start waiting for {sec}")
    await asyncio.sleep(sec) # or any async
    print(f"done waiting for {sec}")
    return sec

async def main():
    print('launched')

    print('starting and awaiting both')
    finished, unfinished = await asyncio.wait(
        [
          asyncio.create_task(do_work(2)),
          asyncio.create_task(do_work(1))
      ],
      return_when=asyncio.FIRST_COMPLETED
    )
    for t in unfinished:
        t.cancel()
    print('finished')
    print(f"finished: {finished.pop().result()}")
    # assume there's only one

asyncio.run(main())
