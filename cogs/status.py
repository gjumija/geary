# status.py
import discord
from discord.ext import commands, tasks

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._join_remove_channel_id = 829970999788699708

    ################################## Basic log
    @commands.Cog.listener()
    async def on_member_join(self, member):
<<<<<<< HEAD
        if member.bot: return
        chnl = self.client.get_channel(self._join_remove_channel_id)
        await chnl.send(f'{member.mention} se připojil k fsociety.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.bot: return
        chnl = self.client.get_channel(self._join_remove_channel_id)
        await chnl.send(f'{member.mention} opustil fsociety.')
=======
        await ctx.send(f'{member.mention} se připojil k fsociety.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await ctx.send(f'{member.mention} opustil fsociety.')
>>>>>>> dc213e837401be72a7630b455d5a2b77ed05a9d4

    ################################## Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)} ms')

    ################################## Clear
    @commands.command(aliases=['c', 'clr'])
    async def clear(ctx, amount=2):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Status(client))
