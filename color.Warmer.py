#!/usr/bin/python3
from kasa import SmartBulb
import asyncio

async def runit():
    bulb = SmartBulb("10.0.0.201")
    bulb2 = SmartBulb("10.0.0.202")
    await bulb.update()
    await bulb2.update()
    newTemp1 = max(bulb.color_temp-500, bulb.valid_temperature_range.min)
    newTemp2 = max(bulb2.color_temp-500, bulb2.valid_temperature_range.min)
    await bulb.set_color_temp(newTemp1, transition=0)
    await bulb2.set_color_temp(newTemp2, transition=0)
    await bulb.update()
    await bulb2.update()

asyncio.run(runit())