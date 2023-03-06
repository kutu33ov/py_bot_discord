import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

intents = discord.Intents().all()
client = discord.Client(intents=intents)

class Mutehelp(commands.Cog): 
	def __init__(self, client):
		self.client = client





def setup(client):
	client.add_cog(Mutehelp(client))
	print('MutehelpCOG: activated')