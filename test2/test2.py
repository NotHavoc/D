import os
import discord
import datetime
import copy
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions
from random import choice

class Test2:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""
        str = "I can do stuff
        #Your code will go here
        await self.bot.say("I can do stuff!")
        
    async def on_message(message):
        """channel = message.channel
        author = message.author

        if message.server is None:
            return

        if author == self.bot.user:
            return

        if not self.bot.user_allowed(message):
            return
                """
        await self.bot.say("does this do shit now?")

def setup(bot):
    bot.add_cog(Test2(bot))
