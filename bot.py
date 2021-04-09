# bot.py
import discord, time, os

from discord.ext import commands, tasks
from datetime import datetime
from dotenv import load_dotenv

print('Bot is ready.')
start_time = time.time()

################################## Basic config
client = commands.Bot(command_prefix=",")
client = discord.Client()

################################## Cog loader
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

################################## Token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

################################## Events
@client.event
async def on_ready():
    print(f'{client.user.name} se připojil!')

################################## Token
client.run(TOKEN)
