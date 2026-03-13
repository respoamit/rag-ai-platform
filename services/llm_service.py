import asyncio

async def generate(prompt):

    await asyncio.sleep(1)

    return f"Generated answer based on: \n{prompt}"
