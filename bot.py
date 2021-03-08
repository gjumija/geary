# bot.py
import discord, time, os 
from discord.ext import commands
from datetime import datetime

print(Bot is ready.)
start_time = time.time()


client = commands.Bot(command_prefix=",")

################################ Cog loader
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

################################# Token
client.run('token')
