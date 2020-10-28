import asyncio
import aiohttp

urls = ['https://cdn.jpegmini.com/user/images/slider_puffin_before_mobile.jpg'] * 10


def save(file, filename: str):
    with open(filename, 'wb') as file_:
        file_.write(file)


async def make_request(url: str, session: aiohttp.ClientSession, filename: str):
    async with session.get(url) as response:
        file = await response.content.read()
        save(file, filename)
        return filename


async def make_requests():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for id_, u in enumerate(urls):
            t = asyncio.create_task(make_request(u, session, f'f{id_}.jpg'))
            tasks.append(t)

        results = await asyncio.gather(*tasks)
        print(results)


asyncio.run(make_requests())




