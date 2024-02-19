import asyncio

async def func1():
    await asyncio.sleep(1)
    print("func1")
    return "Joel"

async def func2():
    await asyncio.sleep(1)

    print("func2")
    
async def func3():
    await asyncio.sleep(4)

    print("func3")
    
async def main():
#     task = asyncio.create_task(func1())
#     await func1()
#     await func2()
#     await func3()
    L = await asyncio.gather(
        func1()
        , func2(),
        func3()
    )

# asyncio.run(main())
    # print(L)



asyncio.run(main())