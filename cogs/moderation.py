import discord
import random
import asyncio
from discord.ext import commands, tasks
import os
import time
from discord.utils import get


class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client


	# @commands.command(alieses = 'mute')
	# @commands.has_permissions(manage_roles = True)
	# async def info(self, ctx,member:disocrd.Member):


	@commands.command(alieses = 'mute')
	@commands.has_permissions(manage_messages = True)
	async def mute (self, ctx, member:discord.Member, time:int, reason):

		report = self.client.get_channel(806145729532919818)
		log = self.client.get_channel(820238510736146472)
		mute_channel = self.client.get_channel(859900812218204170)

		mute_role = discord.utils.get(ctx.guild.roles, name='Преступник')
		
		emb = discord.Embed(title = 'Мут',
							colour = discord.Colour.green()
							)
		emb.add_field(name = 'Модератор/Хелпер', value = ctx.message.author.mention, inline = False)
		emb.add_field(name = 'Нарушитель', value = member.mention, inline = False)
		emb.add_field(name = 'Причина', value = reason, inline = False)
		emb.add_field(name = 'Время', value = time, inline = False)


		await report.send(embed = emb)
		await log.send(f'**Мут**\n**moder:** {ctx.author.mention}\n**muted:** {member.mention}\n\n**Причина:** ```{reason}```\ntime: `{time}`')
		await member.add_roles(mute_role)
		await mute_channel.send(f'{member.mention} ну ты даёшь конечно, ану давай оправдывайся.')

		await asyncio.sleep(time * 60)
		await member.remove_roles(mute_role)
		await report.send(f'{member.mention}, у тебя снялся мут.')

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def unmute(self, ctx, member: discord.Member):
		report = self.client.get_channel(806145729532919818)
		mutedRole = discord.utils.get(ctx.guild.roles, name='Преступник')

		await member.remove_roles(mutedRole)
		await report.send(f"Администрация сняла мут у {member.mention}")



def setup(client):
	client.add_cog(Moderation(client))
	print("Moderation: activated")