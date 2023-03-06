import discord
import os
from discord.ext import commands

class Deleted(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content.startswith('!deleteme'):
			msg = await message.channel.send(
				'I will delete myself now...'
				)

			await msg.delete()

			# this also works
			await message.channel.send(
				'Goodbye in 3 seconds...', delete_after=3.0
				)

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		mention = message.author.mention
		channelLog = self.client.get_channel(
			847965738123788288
			)

		fmt = '{0.author}  удалил сообщение:\n```{0.content}```'
		await channelLog.send(fmt.format(message))



def setup(client):
	client.add_cog(Deleted(client))
	print('Deleted: activated')
