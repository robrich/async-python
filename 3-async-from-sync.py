import asyncio

async def my_fn():
    print('runs')
    await asyncio.sleep(1)
    print('still run')

def main():
    asyncio.run(my_fn())
    print('main is running')

main()
