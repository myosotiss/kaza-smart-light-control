#!/usr/bin/python3
from kasa import SmartBulb
import asyncio


async def runit():
    bulb = SmartBulb("10.0.0.201")
    bulb2 = SmartBulb("10.0.0.202")
    await bulb.update()
    await bulb2.update()

    await bulb.set_color_temp(bulb.valid_temperature_range.min)
    await bulb2.set_color_temp(bulb2.valid_temperature_range.min)
    await bulb.update()
    await bulb2.update()

    await bulb.set_brightness(100)
    await bulb2.set_brightness(100)
    await bulb.update()
    await bulb2.update()

asyncio.run(runit())
