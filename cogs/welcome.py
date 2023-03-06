import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

intents = discord.Intents().all()
client = discord.Client(intents=intents)


class Welcome(commands.Cog): 
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_member_join(self, member):
		welcome = 'Чтобы попасть на сервер тебе нужно пройти верификацию. Ты готов?\n`по возможности ответь "да, хорошо"`'
		channel_age = self.client.get_channel(847966940844261448)
		embed=discord.Embed(title=f"{member.name} добро пожаловать на сервер!", 
							description=f"{member.guild.name} приветствует тебя!") # F-Strings!
		embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!

		await channel_age.send(embed=embed)
		await channel_age.send(welcome)

     
	def check(self, message):
	    try:
	        int(message.content)
	        return True
	    except ValueError:
	        return False

	@commands.Cog.listener()
	async def on_message(self, message):


		verify_context = [
		'да','da', 'yes', 'я тут', 'ок','хорошо'
		]

		channels = ['welcome']
		verify_command = ['no have commands yet']

		role_new = discord.utils.get(
			message.guild.roles, name = 'Верификация'
			)
		role_verify = discord.utils.get(
			message.guild.roles, name = 'проверка возраста'
			)

		role_member = discord.utils.get(
			message.guild.roles, name = 'Новичок'
			)
		


		if str(message.channel) in channels:
			if message.author == self.client.user:
				return


			msg = message.content.lower()
			# if any(word in msg for word in hello):
			# 	await message.channel.send('Привет!')

			

			if any(word in msg for word in verify_context):
				await message.add_reaction("✅")
				await message.channel.send('Отлично, давайте продолжим..')
				time.sleep(1)
				await message.channel.send('Только отвечайте пожалуйста адекватно, Вас будет проверять администрация!')
				time.sleep(2)
				await message.channel.send('Сколько Вам лет?\n`отвечайте цифрой пожалуйста`')
				

				age_min = 14
				age_max = 50

				msg = await self.client.wait_for('message', check=self.check)
				attempt = int(msg.content)

				

				if attempt < age_min:
					await message.channel.send('Извини, но на сервере есть ограничение по возрасту. 14+')
					await msg.add_reaction("❌")

					channelAge = self.client.get_channel(820238510736146472)
					mention = message.author.mention

					await channelAge.send(f'**[**{mention} `проверку возраста НЕ прошёл ❌`**]**\n*input age*: ' + str(attempt))

					time.sleep(3)

					black_list = self.client.get_channel(847976720430268438)
					black_list_role = discord.utils.get(message.guild.roles, name = 'OFFLINE')

					await message.author.add_roles(black_list_role)
					await message.author.remove_roles(role_verify)					

				if attempt >= age_min and attempt < age_max:
					
					
					administration = discord.utils.get(
						message.guild.roles, name = 'Администрация-Палачи'
						)
					channelin = self.client.get_channel(818241897624764417)
					mention = message.author.mention

					await msg.add_reaction("✅")
					message_react = await message.channel.send(
						f'Отлично! Сейчас я вас перенаправлю на администрацию сервера..\nОжидайте..')
					# time.sleep(1)
					# await message.author.add_roles(role_new)
					# await message.author.remove_roles(role_verify)

					await message_react.add_reaction("🔑")
					dot = await message.channel.send('`.`')
					await channelin.send(
						f'{mention} проверку возраста прошёл ✅ \n{administration.mention}, направляю его в <#819306461641179197>\nЖдите..\n**input age**: ' + str(attempt))

					
					await asyncio.sleep(0.5)
					await dot.edit(content='`..`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`...`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`.`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`..`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`...`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`.`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`..`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`...`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`.`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`..`')
					await asyncio.sleep(0.5)
					await dot.edit(content='`...`')
					await asyncio.sleep(0.5)
					await dot.edit(content=f'`Done.`')

					
					time.sleep(5)
					await message.author.add_roles(role_new)
					await message.author.remove_roles(role_verify)
					channelVerify = self.client.get_channel(819306461641179197)
					

					await channelVerify.send(f'{mention} Hello! Здесь тебя проверит {administration.mention}')
					embed=discord.Embed(title=f"Добро пожаловать на сервер!",
										colour = discord.Color.green(),
										description=f"Сейчас у тебя роль {role_new.mention} \nДля того чтобы начать общение, тебе нужно пройти эту верификацию и получить роль {role_member.mention}. \n{administration.mention} помогут тебе в этом. Удачи! \n\n**Ответь на эти вопросы, пожалуйста:** \n**1**. Как ты узнал о тульповодстве в целом? \n**2. У тебя есть тульпа? (Если нет - отправляй только 1,2,6 вопрос. Если есть - отвечай на всё!)**\n**3**. Форсишь ли ты сейчас? Если да, то как ты это делаешь? Опиши свои этапы погружения/визуализации.\n**4**. Есть ли у тебя вондер? Если да, то как ты его создал? (по возможности опиши этапы)\n**5**. Готов ли ты давать советы? Или ты пришёл к нам за опытом?\n**6**. Опиши вкратце, как ты понимаешь феномен Тульп.") # F-Strings!
					 # Set the embed's thumbnail to the member's avatar image!

					await channelVerify.send(embed=embed)





				elif attempt > age_max:
					await message.channel.send('Дедуля, иди-ка ты отсюда.')

					channelAge = self.client.get_channel(820238510736146472)
					mention = message.author.mention

					await channelAge.send(f'**[**{mention} `проверку возраста НЕ прошёл ❌`**]**\n*input age*: ' + str(attempt))

					time.sleep(3)

					black_list = self.client.get_channel(847976720430268438)
					black_list_role = discord.utils.get(message.guild.roles, name = 'OFFLINE')

					await message.author.add_roles(black_list_role)
					await message.author.remove_roles(role_verify)

				
				else:
					error = await message.channel.send('Бип-буп...? :(')
					await error.add_reaction("❓")






def setup(client):
	client.add_cog(Welcome(client))
	print('Welcome: activated')