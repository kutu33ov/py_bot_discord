import discord
import random
import asyncio
from discord.ext import commands, tasks
import os




class Hello(commands.Cog):
	def __init__(self, client):
		self.client = client

	def check(self, message):
		try:
			int(message.content)
			return True
		except ValueError:
			return False

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content.startswith('!in'):
			guild_name = ("Бородинский Клуб Шизоидов")

			await message.author.send("**Поздравляю!**\nТы на сервере " 
			+ guild_name + "\nhttps://www.youtube.com/channel/UC29HcdEnImc2pcG9PhNSHMw\n**kutu33ov приветствует тебя!**")

			mention = message.author.mention
			await message.channel.send(f'`verification scan.....` {mention}\n`role` = <@&805781039876276274>\n**<@&844177932996837406> выдайте роль.**')

		hello_quotes = ['добрый вечер', 'доброе утро', 'добрый день', 
						'день добрый', 'утро доброе', 'вечер добрый', 'здравствуйте', 
						'охаё', 'здарова', 'дарова', 'даров']
		hello_answer = ['Привет 💚','хэй ❤','ХЭЛЛОУ😛', 'Здравствуйте.',
						'ты мне?', 'я тут']

		if message.author == self.client.user:
			return

		msg = message.content.lower()
		mention = message.author.mention

		if any(word in msg for word in hello_quotes):
			await message.channel.send(f'{mention} ' + random.choice(hello_answer))

		hello_react = ['ку', 'приветули', 'привет', 'приветствую', 'татар', 'tatar', 't@t@r',
						'тульпа', 'цыган']

		cloun_react = ['лекс', 'lex', 'клоун', 'цыган', 'cigan', 'кузов', 'gypsi', 'модер']
		emoji = ['🤪', '💤', '🤡', '✌', '👌']

		cloun = ['🤡']

		if any(word in msg for word in hello_react):
			await message.add_reaction(random.choice(emoji))
		if any(word in msg for word in cloun_react):
			await message.add_reaction(random.choice(cloun))

		mention_answer = ['Да, я тут, чо?','**.help**','`.help` - чекниии', 'Вам скучно или чо?', 'ЧО БЛИН?', 'Все вопросы к Кузову',
							'бип-буп?', '!";:%?**:**%^*   ????', 'Ещё раз пинганёшь - бан', 'no', 'yes',
							'возможно', 'ahahahahhaahahhahhahah', 'фе']
		mention_mat = ['пидар','иди нахуй']
		# Don't respond to ourselves
		if message.author == self.client.user:
			return

		# If bot is mentioned, reply with a message
		if self.client.user in message.mentions:
			await message.channel.send(random.choice(mention_answer))
			if any(word in msg for word in mention_mat):
				await message.channel.send('@##$%')

				


		





def setup(client):
	client.add_cog(Hello(client))
	print("HelloCog: activated")