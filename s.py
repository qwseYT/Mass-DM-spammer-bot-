import discord
import asyncio
from discord.ext import commands

TOKEN = 'token'
CHANNEL_ID = id
MESSAGE_TEMPLATE = "MESSAGE"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        members = channel.members
        for member in members:
            try:
                message = MESSAGE_TEMPLATE.format(user_mention=member.mention)
                await member.send(message)
                print(f'Sent message to {member.name}')
            except Exception as e:
                print(f'Could not send message to {member.name}: {e}')
            await asyncio.sleep(2)
    else:
        print(f'Channel with ID {CHANNEL_ID} not found')

    await bot.close()

bot.run(TOKEN)
