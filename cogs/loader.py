# loader.py
import discord
from discord.ext import commands, tasks

class Loader(commands.Cog):
    """docstring for Loader."""

    def __init__(self, client):
        self.client = client
        self._join_remove_channel_id = 829970999788699708

    ################################## Cog loader
    @commands.command()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')

    @commands.command()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')

def setup(client):
    client.add_cog(Loader(client))
