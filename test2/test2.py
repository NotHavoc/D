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
                #await self.bot.send_message(channel, "message.server is None my dudes.")  
                return

            if author == self.bot.user:
                #await self.bot.send_message(channel, "author == self.bot.user my dudes.")  
                return
"""
            if not self.bot.user_allowed(message):
                await self.bot.send_message(channel, "not self.bot.user_allowed(message) my dudes.")  
                return
"""
            if datetime.datetime.now().isoweekday() != 3:
                self.triggered = 0
                await self.bot.send_message(channel, "datetime.datetime.now().isoweekday() != 3 my dudes.")
                return

            if triggered == 0:            
                await self.bot.send_message(channel, "It is Wednesday my dudes.")    
                self.triggered = 1

def setup(bot):
    bot.add_cog(Test2(bot))
