import asyncio
from easy_sync import sync_compatible

@sync_compatible
async def async_add(a: int, b: int) -> int:
    ''' Add two numbers asynchronously '''
    await asyncio.sleep(0.1)
    return a + b

def test_simple_case():

    def do_sync():

        print(async_add(1, 2).wait())
        print(async_add(3, 4).wait())

    do_sync()

    async def async_main():
        result = await async_add(1, 2)
        print(result)

    asyncio.run(async_main())
