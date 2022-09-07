import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1) # second
    print('world')

asyncio.run(main())
