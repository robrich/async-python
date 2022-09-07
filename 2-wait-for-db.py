import asyncio
import aiomysql # async MySQL lib

async def test_example():
    pool = await aiomysql.create_pool(...)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
          await cur.execute("SELECT 42;")
          print(cur.description)
          (r,) = await cur.fetchone()
          assert r == 42
    pool.close()
    await pool.wait_closed()

asyncio.run(test_example())
