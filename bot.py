import discord
from discord.ext import commands
import os
import asyncio
import random
from aioconsole import ainput

intents = discord.Intents().all()
client = commands.Bot(command_prefix = ".", intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
	print('\nThe BOT is connected to the system.')
	print('Commands for COGS:\nload | unload | reload')


@client.command()
async def help(ctx):
	emb = discord.Embed(title = 'Помощь по командам', 
						colour = discord.Colour.green()
						)

	emb.add_field(name = 'Coins',
				value = '`.timely` - **получить коины** *(интервал 12 часов)*\n\n`.balance` - **проверить свой баланс.**\n`.give <@имя> <кол-во>` - **передать человеку коины.**\n\n`.shop` - **магазин.**',
				)
	await ctx.send(embed = emb)

@client.command()
async def load(ctx, extension):
	if ctx.author.id == 591597695949471764:
		client.load_extension(f"cogs.{extension}")
		await ctx.send("COG: loaded")
	else:
		await ctx.send("Вы не создатель бота")

@client.command()
async def reload(ctx, extension):
	if ctx.author.id == 591597695949471764:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		await ctx.send("COG: reload")
	else:
		await ctx.send("Вы не создатель бота")

@client.command()
async def unload(ctx, extension):
	if ctx.author.id == 591597695949471764:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send("COG: disabled")
	else:
		await ctx.send("Вы не создатель бота")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")



async def chng_pr():
	await client.wait_until_ready()

	statuses = ['.help', '.timely - ЗАБЕРИ БОНУС + COINS',
				'А ты точно подписан на канал Кутузова? Подпишись скорее: https://www.youtube.com/c/Kutuzov-Inculcation',
				'Я слежу за сервером!!!!']

	while not client.is_closed():
		statusGame = random.choice(statuses)

		await client.change_presence(status = discord.Status.dnd, activity = discord.Game(statusGame))
		await asyncio.sleep(15)

client.loop.create_task(chng_pr())



#client.run('ODQ2NTMzNzAwMTc4NjczNjY0.YKw58Q.qdIYaHCcPXR65H_koOTf6Mj7JfU')
client.run('ODQyMzkzMjA5NDA0MzkxNDU1.YJ0p0A.aNo9mklK9rtamexMOuKsi45tGvU')