import math
from asyncio import sleep

from utils.helpers import *
import asyncio


def log(msg: str):
    line = f'{clock()} {msg}'
    buf.log(line)


class BufLogger:
    def __init__(self):
        self.lines = ['' for _ in range(100)]
        self.N = 100
        self.i = 0

    def log(self, msg):
        self.lines[self.i % self.N] = msg
        self.i += 1

    def print(self):
        for i in range(self.i):
            print(self.lines[i])
        self.i = 0


buf = BufLogger()

async def boil_water():
    log("boiling water for cofee")
    await sleep(0.3)
    log("water boiled for cofee")

async def make_cofee()-> str:
    log('making cofee')
    water = await boil_water()
    log('start making cofee')
    await sleep(0.2)
    log('cofee done')
    return 'cofee'

async def cut_bread() -> str:
    log('cuting bread')
    await sleep(0.1)
    log('chleb pokrojony')
    return 'bread'

async def prepare_bread() -> str:
    log('preparing bread')
    bread = await cut_bread()
    log('mam chleb')
    await sleep(0.1)
    log('mam posmarowany chleb')
    return "good_bread"

async def boil_eggs():
    log("boiling water for eggs")
    await sleep(0.4)
    log("eggs boiled")

async def nakryj_stol():
    log('nakrywanie stołu')

async def scheduler():
    log(f'main; task:{task_name()}')
    a = asyncio.create_task(boil_eggs())
    b = asyncio.create_task(prepare_bread())
    c = asyncio.create_task(make_cofee())



    await asyncio.gather(a,b,c)
    log('skonczone')





if __name__ == '__main__':
    asyncio.run(scheduler())  # tworzy event loop
    buf.print()

# async def butter_bread() -> str:
#     log('smarowanie chleba')
#     bread = await prepare_bread()
#     log('')
#     await sleep(0.1)
#     log('chleb posmarowany')
#     return 'good_bread'