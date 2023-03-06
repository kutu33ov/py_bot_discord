import discord
import random
import asyncio
from discord.ext import commands, tasks
import os
import time
from discord.utils import get



class Verification(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command(alieses = 'add')
	@commands.has_permissions(manage_messages = True)
	async def add(self, ctx, member: discord.Member):
		# if message.author == self.client.user:
		# 	return

		channelScan = self.client.get_channel(819306461641179197)
		
		await channelScan.send(f'`verification scan::` {member.mention}\n`role`:: **<@&805781039876276274>**', delete_after=60)
		time.sleep(2)
		message = await channelScan.send('`.`')
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
		await message.edit(content=f'`Done.` {member.mention}')


		role_verify = discord.utils.get(ctx.guild.roles, name='Верификация')
		role_newMember = discord.utils.get(ctx.guild.roles, name='Новичок')

		await member.remove_roles(role_verify)
		await member.add_roles(role_newMember)
 
		channelBot = self.client.get_channel(806145729532919818)

		emb = discord.Embed(title = 'Добро пожаловать!', 
							description = '**Бородинский Клуб Шизоидов приветствует тебя!**\nПрочитай __внимательно__ <#621033332469268500> это очень **важно**.\n<#807094314488168469> - вся информация по вопросам.\n<#806212340176650270> - выбери себе роль.\nЕсли у тебя есть вопросы - <@&844177932996837406>',
							colour = discord.Color.green(), 
							url = 'https://www.youtube.com/channel/UC29HcdEnImc2pcG9PhNSHMw')

		await channelBot.send('🔥 ' f'{member.mention} 🔥')
		await channelBot.send(embed = emb)
		await channelBot.send(
	    	f'**Проверку реализовал **' + f'{ctx.author.mention} ✅')

		channelCommunication = self.client.get_channel(806241086921375814)
		welcome_member = ['теперь в чате.', 'залетает на сервер.', 'прошёл верификацию.', 'ЗДАРОВА! МЫ РАДЫ ТЕБЯ ВИДЕТЬ']

		await channelCommunication.send(
	    	f'{member.mention} ' + random.choice(welcome_member))

		print(f'\nVerification: Member: {member}\n              Admin: {ctx.author}')

	@commands.command()
	@commands.has_permissions(manage_messages = True)
	async def done(self, ctx, *, text):

		channel_log = self.client.get_channel(820238510736146472)
		message = await channel_log.send(f'{text}\n{ctx.author.mention} проверил✅\n\nВерификация пройдена!✅')
		await message.add_reaction("✅")

	# @commands.command()
	# @commands.has_permissions(manage_messages = True)
	# async def out(self, ctx, member: discord.Member):

	# 	role_verify = discord.utils.get(ctx.guild.roles, name='проверка возраста')
	# 	role_newMember = discord.utils.get(ctx.guild.roles, name='')
def setup(client):
	client.add_cog(Verification(client))
	print("VerificationCog: activated")