import discord
from discord.ext import commands

class Avatar(commands.Cog):
  def __init__(self, client):
		self.client = client

	@commands.command(aliases = ['аватар'])
	async def avatar(self, ctx):
		await ctx.send(ctx.author.avatar_url)

def setup(client):
	client.add_cog(Avatar(client))
	print("AvatarCog: activated")
