#!/usr/bin/python3
from kasa import SmartBulb
import asyncio


async def runit():
    bulb = SmartBulb("10.0.0.201")
    bulb2 = SmartBulb("10.0.0.202")
    await bulb.update()
    await bulb2.update()

    await bulb.turn_off()
    await bulb2.turn_off()
    await bulb.update()
    await bulb2.update()


asyncio.run(runit())
