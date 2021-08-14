# loader.py
import discord
from discord import commands, tasks

class Status(object):
    """docstring for Status."""

    def __init__(self, client):
        self.client = client
        self._join_remove_channel_id = 829970999788699708

    ################################## Cog loader
    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')

    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')

def setup(client):
    client.add_cog(Status(client))
