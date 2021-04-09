#hello.py
import discord
from discord.ext import commands, tasks

class Alizee(commands.Cog):
    """docstring forAlizee."""

    def __init__(self, client):
        self.client = client
        self._join_remove_channel_id = 829970999788699708

    players = {}

    ################################### Alizee
    @commands.command(pass_context=True)
    async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)

    @commands.command(pass_context=True)
    async def leave(ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        await voice_client.disconnect(channel)

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

def setup(client):
    client.add_cog(Alizee(client))
