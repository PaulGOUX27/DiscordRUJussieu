import os
import discord
import yaml
from pyBurger import *

from discord.ext import commands
from collections import defaultdict

config = yaml.safe_load(open("config.yml"))
token = config["token"]

emojiDic = defaultdict(str)
emojiDic.update(zip("pizza burger".split(), "🍕 🍔".split()))

client = discord.Client()

@client.event
async def on_ready():
    print('{client.user.name} has connected to Discord!')

bot = commands.Bot(command_prefix='$')

def extractEmote(string):
	#Du python de haut nuveau, par un eskérien
	return ''.join(emoji for key, emoji in emojiDic.items() if key in string.lower())

@bot.command(name='menu', help='Affiche le menu du RU de Jussieu')
async def menu(ctx):
	menu = getMenuCurrentDay()
	string = "Repas du " + menu.date + "\r\n"
	string += "Plat principal \r\n"
	for plat in menu.plats:
		string += " - "
		string += plat
		string += extractEmote(plat)
		string += "\r\n"

	string += "Desserts : \r\n"
	for dessert in menu.desserts:
		string += " - "
		string += dessert
		string += "\r\n"
	await ctx.send(string)

bot.run(token)

