# status.py
import discord
from discord.ext import commands, tasks

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

################################## Basic log
@commands.Cog.listener()
async def on_member_join(self):
    await ctx.send(f'{member.mention} se připojil fsociety.')

@client.event
async def on_member_join(self, member):
    await ctx.send(f'{member.mention} se připojil k fsociety.')

@client.event
async def on_member_rmeove(self, member):
    await ctx.send(f'{member.mention} opustil fsociety.')

################################## Ping
@client.command()
async def ping(self, ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

################################## Clear
@client.command(aliases=['c', 'clr'])
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Status(client))
