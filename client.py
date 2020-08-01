#Импортируем необходимые библиотеки
import discord
from discord.ext import commands
import asyncio

#Импортируем второстепенные библиотеки
import random 
import colorama
from colorama import Fore, Style
from random import randint

#Инициализируем колораму
colorama.init()

#Настройка конфигурации
from config import *

token = settings["TOKEN"] #Получаем токен из словаря settings по ключу "TOKEN"
prefix = commands.when_mentioned_or(settings["PREFIX"]) #Получаем префикс

bot = commands.Bot(command_prefix = prefix) # Назначение префикса бота
bot.remove_command("help")
# %help

#Пока бот стартует и запускает всю систему
@client.event
async def on_connect():
	print(f'{Fore.YELLOW}=========================')
	print(f'Connection to discord.com')
	print(f'Token: {token}')
	print(f'ID: {client.user.id}')
	print('Prefix: {prefix}')
	print(f'{Fore.YELLOW}=========================')

	await self.client.change_presence(status = discord.Status.idle, activity = discord.Game(name = "Zzzzzz..."))

#Когда бот готов работать
@client.event
async def on_ready():
	print(f'{Fore.GREEN}=========================')
	print(f'Bot logged in as - ')
	print(f'Username: {client.user.name}')
	print(f'ID: {client.user.id}')
	print(f'{Fore.GREEN}=========================')

	a = randint(1,2)

	if a == 1:
		await self.client.change_presence(status = discord.Status.online, activity = discord.Game(name = prefix + config.gaming))

		print("Bot playing!")
	else:
		await self.client.change_presence(status = discord.Status.online, activity = discord.Activity(name = config.invite, type = discord.ActivityType.listening))

		print("Bot listening invite!")

@bot.command()  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
	
	await ctx.send(arg)  # отправляем обратно аргумент
# Команда $test. Повторяет аргумент пользывателя 

#пак команд на коги: загрузка кога, выгрузка, перезагрузка и перезагрузка всех когов

#cog load
@client.command(aliases = ['cog_load', 'load'])
@command.is_owner()
async def __load(ctx, extensions):
	client.load_extension(f'cogs.{extensions}')

#cog unload
@client.command(aliases = ['cog_unload', 'unload'])
@command.is_owner()
async def __unload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')

#cog reload
@client.command(aliases = ['cog_reload', 'reload'])
@command.is_owner()
async def __reload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')
    client.load_extension(f'cogs.{extensions}')
    
#cogs reload
@client.command(aliases = ['cogs_reload_all', 'reload_all'])
@command.is_owner()
async def __reloadall(ctx):
	for filename in os.listdir('./cogs'):
   	 if filename.endswith('.py'):
        	client.load_extension(f'cogs.{filename[:-3]}')


if __name__ == "__main__":
	bot.run(token)