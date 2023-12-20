#!/usr/bin/python3
from kasa import SmartBulb
import asyncio
import time
import random

async def runit():
    bulb = SmartBulb("10.0.0.201")
    bulb2 = SmartBulb("10.0.0.202")
    await bulb.update()
    await bulb2.update()
    h = random.randrange(360)
    s = random.randrange(101)
    await bulb.set_hsv(h, s, 100, transition=500)
    await bulb2.set_hsv(random.randrange(360), random.randrange(101), 100, transition=500)
    await bulb.update()
    await bulb2.update()

    time.sleep(0.5)
asyncio.run(runit())
