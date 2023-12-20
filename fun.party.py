#!/usr/bin/python3
from kasa import SmartBulb
import asyncio
import time
import random

# asyncio.run(bulb.set_brightness(100, transition=0))
# asyncio.run(bulb2.set_brightness(100, transition=0))
# asyncio.run(bulb.update())
# asyncio.run(bulb2.update())


async def runit():
    bulb = SmartBulb("10.0.0.201")
    bulb2 = SmartBulb("10.0.0.202")
    await bulb.update()
    await bulb2.update()
    for i in range(5):
        t = 0
        h = random.randrange(360)
        s = random.randrange(101)
        v = random.randrange(101)
        await bulb.set_hsv(h, s, v, transition=t)
        await bulb2.set_hsv(h, s, v, transition=t)
        await bulb.update()
        await bulb2.update()
        time.sleep(t/1000 + 0.5)
asyncio.run(runit())
