import asyncio
import aiohttp
from fun import *
NAME20_CC = [str(x+1) for x in range(20)]


@asyncio.coroutine
def multi_get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    image = yield from resp.read()
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from multi_get_flag(cc)
    show(cc)
    save_img(image, cc.lower() + '.jpg')
    return cc


def multi_download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)


def multi_main(download_many, pic_name=NAME20_CC):
    t0 = time.time()
    count = download_many(pic_name)
    elapsed = time.time() - t0
    msg = '\n{} pic downloaded in {:.2f}s'
    print(msg.format(count, elapsed))

