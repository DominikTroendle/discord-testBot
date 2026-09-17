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

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Bot')
    if not role:
        await ctx.send("Die Rolle wurde nicht gefunden!")
        return
    await ctx.author.add_roles(role)
    await ctx.send(f"{ctx.author.mention} wurde die Rolle '{role}' hinzugefügt!")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Bot')
    if not role:
        await ctx.send("Die Rolle wurde nicht gefunden!")
        return
    await ctx.author.remove_roles(role)
    await ctx.send(f"Die Rolle '{role}' wurde von {ctx.author.mention} entfernt!")

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