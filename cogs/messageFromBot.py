import discord
import asyncio
from discord.ext import commands, tasks
import os



class MessageFromBot(commands.Cog):
	def __init__(self, client):
		self.client = client



	@commands.command(alieses = 'message_comm')
	@commands.has_permissions(administrator = True, manage_messages = True)

	async def v(self, ctx, *, args):
		channel = self.client.get_channel(819306461641179197)
		await channel.send("{}".format(args))



	@commands.command(alieses = 'say')
	@commands.has_permissions(administrator = True)

	async def say(self, ctx, channel: discord.TextChannel, *args):

		text = ''
		for item in args:
			text = text + item + ' '
		await channel.send(text)


def setup(client):
	client.add_cog(MessageFromBot(client))
	print('MessageFromBot: activated')
