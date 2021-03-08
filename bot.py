# bot.py
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix=",")

################################ Cog loader
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

################################# Token
client.run('token')
