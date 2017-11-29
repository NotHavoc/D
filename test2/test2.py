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

class Test2:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.triggered = 0
         

    @commands.command()
    async def test(self):
        """This does stuff!"""
        str = "Triggered value:"
        #Your code will go here
        await self.bot.say(str)
        await self.bot.say(self.triggered)
        
    async def on_message(self, message):
            channel = message.channel
            author = message.author

            if message.server is None:
                return

            if author == self.bot.user:
                return

            if not self.bot.user_allowed(message):
                return

            if datetime.datetime.now().isoweekday() != 3:
                self.triggered = 0
                #await self.bot.send_message(channel, "It is to some degree not Wednesday my dudes.")
                return

            if triggered == 1:
                return 
            
            await self.bot.send_message(channel, "It is Wednesday my dudes.")    
            self.triggered = 1

def setup(bot):
    bot.add_cog(Test2(bot))
