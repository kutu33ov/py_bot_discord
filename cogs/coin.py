import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import random
import os
import json
import sqlite3


client = commands.Bot(command_prefix = '.',intents=discord.Intents.all())

connection = sqlite3.connect('server.db')
cursor = connection.cursor()

queue = []
class Coin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            id INT,
            cash BIGINT,
            rep INT,
            lvl INT,
            server_id INT
        )""")
     
        cursor.execute("""CREATE TABLE IF NOT EXISTS shop (
            role_id INT,
            id INT,
            cost BIGINT
        )""")
     
        for guild in client.guilds:
            for member in guild.members:
                if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                    cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, 1, {guild.id})")
                else:
                    pass
     
        connection.commit()
        print('client connected')



    @commands.command()
    async def timely(self, ctx):
        with open('economy.json','r') as f:
            money = json.load(f)
        if not str(ctx.author.id) in money:
            money[str(ctx.author.id)] = {}
            money[str(ctx.author.id)]['Money'] = 0

        if not str(ctx.author.id) in queue:
            emb = discord.Embed(description=f'**{ctx.author}** Вы получили свои 5 монет')
            await ctx.send(embed= emb)
            money[str(ctx.author.id)]['Money'] += 5
            queue.append(str(ctx.author.id))
            with open('economy.json','w') as f:
                json.dump(money,f)
            await asyncio.sleep(12*60)
            queue.remove(str(ctx.author.id))
        if str(ctx.author.id) in queue:
            emb = discord.Embed(description=f'**{ctx.author}** Вы уже получили свою награду')
            await ctx.send(embed= emb)
    @commands.command()
    async def balance(self,ctx,member:discord.Member = None):
        if member == ctx.author or member == None:
            with open('economy.json','r') as f:
                money = json.load(f)
            emb = discord.Embed(title = 'BALANCE:',
                                description=f'{ctx.author.mention}\nУ **{ctx.author}** \n\n__**{money[str(ctx.author.id)]["Money"]}**__ **coins**\n\n`.give [nick] [кол-во]` - передать коины человеку',
                                colour = discord.Color.green())
                                
            await ctx.send(embed= emb)
        else:
            with open('economy.json','r') as f:
                money = json.load(f)
            emb = discord.Embed(title = 'BALANCE:',
                                description=f'{member.mention}\nУ **{member}** \n\n__**{money[str(member.id)]["Money"]}**__ **coins**\n\n`.give [nick] [кол-во]` - передать коины человеку',
                                colour = discord.Color.green())
            await ctx.send(embed= emb)
    @commands.command()
    async def addshop(self, ctx,role:discord.Role,cost:int):
        with open('economy.json','r') as f:
            money = json.load(f)
        if str(role.id) in money['shop']:
            await ctx.send("Эта роль уже есть в магазине")
        if not str(role.id) in money['shop']:
            money['shop'][str(role.id)] ={}
            money['shop'][str(role.id)]['Cost'] = cost
            await ctx.send('Роль добавлена в магазин')
        with open('economy.json','w') as f:
            json.dump(money,f)
    @commands.command()
    async def shop(self,ctx):
        with open('economy.json','r') as f:
            money = json.load(f)
        emb = discord.Embed(title="Магазин",
                            colour = discord.Color.green())
        for role in money['shop']:
            emb.add_field(name=f'Цена: {money["shop"][role]["Cost"]}',value=f'<@&{role}>',inline=False)
        await ctx.send(embed=emb)
    @commands.command()
    async def removeshop(self,ctx,role:discord.Role):
        with open('economy.json','r') as f:
            money = json.load(f)
        if not str(role.id) in money['shop']:
            await ctx.send("Этой роли нет в магазине")
        if str(role.id) in money['shop']:
            await ctx.send('Роль удалена из магазина')
            del money['shop'][str(role.id)]
        with open('economy.json','w') as f:
            json.dump(money,f)
    @commands.command()
    async def buy(self,ctx,role:discord.Role):
        with open('economy.json','r') as f:
            money = json.load(f)
        if str(role.id) in money['shop']:
            if money['shop'][str(role.id)]['Cost'] <= money[str(ctx.author.id)]['Money']:
                if not role in ctx.author.roles:
                    await ctx.send('Вы купили роль!')
                    for i in money['shop']:
                        if i == str(role.id):
                            buy = discord.utils.get(ctx.guild.roles,id = int(i))
                            await ctx.author.add_roles(buy)
                            money[str(ctx.author.id)]['Money'] -= money['shop'][str(role.id)]['Cost']
                else:
                    await ctx.send('У вас уже есть эта роль!')
        with open('economy.json','w') as f:
            json.dump(money,f)

    @commands.command(pass_context = True)
    async def give(self,ctx,member:discord.Member,arg:int):


        with open('economy.json','r') as f:
            money = json.load(f)
        if arg >= 1:
            if money[str(ctx.author.id)]['Money'] >= arg:
                emb = discord.Embed(description=f'**{ctx.author}** подарил **{member}**\n\n`{arg}` coin(s)\n\n**BALANCE:**\n**{member.mention}** __**{money[str(member.id)]["Money"]}**__ **coins**\n**{ctx.author.mention}** __**{money[str(ctx.author.id)]["Money"]}**__ **coins**\n\n`.balance` - *проверить кол-во коинов*')
                money[str(ctx.author.id)]['Money'] -= arg
                money[str(member.id)]['Money'] += arg
                await ctx.send(embed = emb)
            else:
                await ctx.send('У вас недостаточно денег')
            with open('economy.json','w') as f:
                json.dump(money,f)
        if arg < 0:
            await ctx.send('Ты не можешь отправить такую сумму.')
        if arg == 0:
            emb = discord.Embed(description=f'**{ctx.author}** подарил **{member}** **{arg}** монет, НОРМ ТРАНЗАКЦИЯ БРО')
            await ctx.send(embed = emb)


    @commands.command()
    @commands.has_permissions(administrator = True)
    async def take(self,ctx,member:discord.Member,arg:int):
        with open('economy.json','r') as f:
            money = json.load(f)

        if arg < 1:
            if money[str(ctx.author.id)]['Money'] >= arg:
                emb = discord.Embed(description=f'**{ctx.author}** забрал у **{member}** **{arg}** монет')
                money[str(ctx.author.id)]['Money'] -= arg
                money[str(member.id)]['Money'] += arg
                await ctx.send(embed = emb)
            else:
                await ctx.send('У вас недостаточно денег')
            with open('economy.json','w') as f:
                json.dump(money,f)
        if arg >= 1:
            await ctx.send('*это действие невозможно сделать, изпользуй* `give`')



    @commands.command(pass_context = True)
    @commands.has_permissions(manage_messages = True)
    async def joke(self,ctx,member:discord.Member,arg:int):


        with open('economy.json','r') as f:
            money = json.load(f)
        
        if money[str(ctx.author.id)]['Money'] >= arg:
            emb = discord.Embed(description=f'**{ctx.author}** подарил **{member}** **{arg}** монет')
            money[str(ctx.author.id)]['Money'] -= arg
            money[str(member.id)]['Money'] += arg
            await ctx.send(embed = emb)
        else:
            await ctx.send('У вас недостаточно денег')
        with open('economy.json','w') as f:
            json.dump(money,f)


    # @commands.command()
    # async def bank(self,ctx,member:discord.Member = None):
    #     if member == ctx.author or member == None:
    #         with open('bank.json','r') as f:
    #             bank = json.load(f)
    #         emb = discord.Embed(title = 'BALANCE:',
    #                             description=f'{ctx.author.mention}\nУ **{ctx.author}** \n\n__**{bank[str(ctx.author.id)]["Money"]}**__ **coins**\n\n`.give [nick] [кол-во]` - передать коины человеку',
    #                             colour = discord.Color.green())
                                
    #         await ctx.send(embed= emb)
    #     else:
    #         with open('economy.json','r') as f:
    #             money = json.load(f)
    #         emb = discord.Embed(title = 'BALANCE:',
    #                             description=f'{member.mention}\nУ **{member}** \n\n__**{money[str(member.id)]["Money"]}**__ **coins**\n\n`.give [nick] [кол-во]` - передать коины человеку',
    #                             colour = discord.Color.green())
    #         await ctx.send(embed= emb)


    # @commands.command()
    # async def leaderboard(self, ctx):
    #     embed = discord.Embed(title = 'Топ 10 сервера')
    #     counter = 0
 
    #     for row in cursor.execute("SELECT name, cash FROM users WHERE server_id = {} ORDER BY cash DESC LIMIT 10".format(ctx.guild.id)):
    #         counter += 1
    #         embed.add_field(
    #             name = f'# {counter} | `{row[0]}`',
    #             value = f'Баланс: {row[1]}',
    #             inline = False
    #         )
 
    #     await ctx.send(embed = embed)



def setup(client):
    client.add_cog(Coin(client))
    print("CoinCog: activated")