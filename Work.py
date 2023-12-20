#!/usr/bin/python3
from kasa import SmartBulb
import asyncio


async def runit():
    bulb = SmartBulb("10.0.0.201")
    bulb2 = SmartBulb("10.0.0.202")
    await bulb.update()
    await bulb2.update()

    h = 0
    s=40
    v=35
    await bulb.set_hsv(h, s, v)
    await bulb2.set_hsv(h, s, v)
    await bulb.update()
    await bulb2.update()


asyncio.run(runit())
