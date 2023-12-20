#!/usr/bin/python3
from kasa import SmartBulb
import asyncio


async def runit():
    bulb = SmartBulb("10.0.0.201")
    bulb2 = SmartBulb("10.0.0.202")
    await bulb.update()
    await bulb2.update()
    await bulb.set_hsv(0, 100, 100, transition=1000)
    await bulb2.set_hsv(240, 100, 100, transition=1000)
    await bulb.update()
    await bulb2.update()

asyncio.run(runit())
