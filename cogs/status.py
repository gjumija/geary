# status.py
import discord
from discord.ext import commands

class Status(commands.Cog):

    def __init__(self, client):
        self.client = client

################################ Bot status
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')

def setup(client):
    client.add_cog(Example(client))
