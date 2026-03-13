import asyncio 

async def stream_response(text):

    for word in text.split():
        await asyncio.sleep(0.2)
        yield word + " "
