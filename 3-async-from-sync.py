import asyncio

async def my_fn():
    print('runs')
    await asyncio.sleep(1)
    print('still run')

def main():
    my_fn() # oops
    print('main is running')

main()
