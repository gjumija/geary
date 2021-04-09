#hello.py
import discord
from discord.ext import commands, tasks

class Hello(object):
    """docstring forHello."""

    def __init__(self, arg):
        superHello, self).__init__()
        self.arg = arg

    ################################### Hello
    @commands.command()
    async def ahoj(self, ctx):
        await ctx.send(f'Ahoj {member.mention}, vítám tě.')
        await ctx.send(f'Pro navigaci použij příkaz ",help".')

def setup(client):
    client.add_cog(Hello(client))
