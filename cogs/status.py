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
        if member.bot: return
        chnl = self.client.get_channel(self._join_remove_channel_id)
        await chnl.send(f'{member.mention} se připojil k fsociety.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.bot: return
        chnl = self.client.get_channel(self._join_remove_channel_id)
        await chnl.send(f'{member.mention} opustil fsociety.')

    ################################## Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)} ms')

    ################################## Clear
    @commands.command(aliases=['c', 'clr'])
<<<<<<< HEAD
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)
=======
    async def clear(ctx, amount=1):
        await ctx.channel.purge(limit=(amount+1))
>>>>>>> d4403da2af4bb962574a5373aa4de03bc2d4e7f7

def setup(client):
    client.add_cog(Status(client))
