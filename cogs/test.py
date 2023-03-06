import discord
from discord.ext import commands
import os
import time
from discord.utils import get
import asyncio


class Test(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command()
	@commands.has_permissions(manage_messages = True)
	async def ok(self, ctx):



		

		message = await ctx.send('`.`')
		await asyncio.sleep(0.5)
		await message.edit(content='`..`')
		await asyncio.sleep(0.5)
		await message.edit(content='`...`')
		await asyncio.sleep(0.5)
		await message.edit(content='`.`')
		await asyncio.sleep(0.5)
		await message.edit(content='`..`')
		await asyncio.sleep(0.5)
		await message.edit(content='`...`')
		await asyncio.sleep(0.5)
		await message.edit(content='`.`')
		await asyncio.sleep(0.5)
		await message.edit(content='`..`')
		await asyncio.sleep(0.5)
		await message.edit(content='`...`')
		await asyncio.sleep(0.5)
		await message.edit(content='`Done.`')

def setup(client):
	client.add_cog(Test(client))
	print("Test: activated")