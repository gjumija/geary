# bot.py
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix=",")

################################ Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


################################# Token
client.run('ODE4MzkwMTA1NjA0NDg5MjI4.YEXXLg.XqxeGm0UpFHcovmopZ43I-PqIiA')
