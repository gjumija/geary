# status.py
import discord
from discord.ext import commands, tasks

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

    ################################## Basic log
    @commands.Cog.listener()
    async def member_join(self, member):
        await ctx.send(f'{member.mention} se připojil k fsociety.')

    @commands.Cog.listener()
    async def member_remove(self, member):
        await ctx.send(f'{member.mention} opustil fsociety.')

    ################################## Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

    ################################## Clear
    @commands.command(aliases=['c', 'clr'])
    async def clear(ctx, amount=2):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Status(client))
