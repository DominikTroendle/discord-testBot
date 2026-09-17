import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import logging

handler = logging.FileHandler(filename='discordbot.log', mode='w', encoding='utf-8')

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")

@bot.command()
async def greet(ctx):
    await ctx.send(f"Servus {ctx.author.mention}!")

@bot.command()
async def recent_message(ctx, arg):
    await ctx.send(f"Deine letzte Nachricht war: {arg}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'python' in message.content.lower():
        await message.delete()
        channel = message.channel
        await channel.send(f"Hey {message.author}, dieser Befehl enthält Zeichen, die nur Devs vorbehalten sind!")
    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)