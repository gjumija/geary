# bot.py
import discord, time, os

from discord.ext import commands, tasks
from datetime import datetime
from dotenv import load_dotenv

################################## Basic config
print('Bot is ready.')
start_time = time.time()

client = commands.Bot(command_prefix="/")

################################## Cog loader
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

################################## Token
load_dotenv()
TOKEN = os.getenv('TOKEN')

################################## Run boy run
client.run(TOKEN)
