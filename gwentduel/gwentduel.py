import os
import discord
import datetime
import copy
import asyncio
import re
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions
from random import choice

class GwentDuel:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=False)
    async def gduel(self, ctx):
        await self.bot.say("may or may not be working")
        values = ctx.split(' ')

        if values.length < 4:
            await self.bot.say("Failed. Call command with power and armor of the two respective units space deliniated")
            return

        atkPower = values.pop(0)
        atkArmor = values.pop(0)
        defPower = values.pop(0)
        defArmor = values.pop(0)

        while atkPower > 0 and defPower > 0:
            if defArmor > 0:
                defArmor -= atkPower
                if defArmor < 0:
                    defPower += defArmor
            else:
                defPower -= atkPower
            if defPower > 0:
                if atkArmor > 0:
                    atkArmor -= defPower
                    if atkArmor < 0:
                        atkPower += atkArmor
                else:
                    atkPower -= defPower

        await self.bot.say("Attacker Power: " + atkPower)
        await self.bot.say("Attacker Armor: " + atkArmor)
        await self.bot.say("Defender Power: " + defPower)
        await self.bot.say("Defender Armor: " + defPower)
        

def setup(bot):
    bot.add_cog(GwentDuel(bot))
