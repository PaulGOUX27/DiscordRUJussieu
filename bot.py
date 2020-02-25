import os
import discord
import yaml

from discord.ext import commands

config = yaml.safe_load(open("config.yml"))
token = config["token"]

client = discord.Client()

bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@bot.command(name='menu', help='Affiche le menu du RU de Jussieu')
async def menu(ctx):
    await ctx.send("Mathieu on need ton code")

bot.run(token)
