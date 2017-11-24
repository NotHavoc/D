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
        self.triggered = false
         

    @commands.command()
    async def test(self):
        """This does stuff!"""
        str = "I can do stuff"
        #Your code will go here
        await self.bot.say(str)
        
    async def on_message(self, message):
       # try
            channel = message.channel
            author = message.author

            if message.server is None:
                return

            if author == self.bot.user:
                return

            if not self.bot.user_allowed(message):
                return

            day = datetime.datetime.now().isoweekday()

            if day != 3
                self.triggered = false
                return

            self.triggered = true
            await self.bot.say("It is Wednesday my dudes.")    

def setup(bot):
    bot.add_cog(Test2(bot))
