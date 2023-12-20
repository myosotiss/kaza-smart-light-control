#!/usr/bin/python3
from kasa import SmartBulb
import asyncio


async def runit():
    bulb = SmartBulb("10.0.0.201")
    bulb2 = SmartBulb("10.0.0.202")
    await bulb.update()
    await bulb2.update()

    v1= (bulb.valid_temperature_range.min + bulb.valid_temperature_range.max)/2
    v2= (bulb2.valid_temperature_range.min + bulb2.valid_temperature_range.max)/2
    await bulb.set_color_temp(v1)
    await bulb2.set_color_temp(v2)
    await bulb.update()
    await bulb2.update()

    await bulb.set_brightness(100)
    await bulb2.set_brightness(100)
    await bulb.update()
    await bulb2.update()

asyncio.run(runit())
