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
bot.remove_command("help") # Удаляет команду help
# %help

#Пока бот стартует и запускает всю систему
@client.event # Создаём событие 
async def on_connect(): # Когда бот подключаеся 
	print(f'{Fore.YELLOW}=========================') # Вывести жёлтую строку
	print(f'Connection to discord.com') # Вывести "подключение к дискорду"
	print(f'Token: {token}') # Вывести токен
	print(f'ID: {client.user.id}') # Вывести id бота 
	print('Prefix: {prefix}') # Вывести префикс бота
	print(f'{Fore.YELLOW}=========================') # Вывести жёлтую строку

	await self.client.change_presence(status = discord.Status.idle, activity = discord.Game(name = "Zzzzzz...")) # Вывести стаутс бота "Zzzzzz..."
# При ПОДКЛЮЧЕНИИ бота выводит выжуню информацию и статус "Zzzzzz..." до полной готовности бота к работе.
 
#Когда бот готов работать
@client.event # Создаём событье 
async def on_ready(): # Когда бот готов
	print(f'{Fore.GREEN}=========================') # Вывести зелёную строку
	print(f'Bot logged in as - ') # Вывести "Бот зарегестрирван как -"
	print(f'Username: {client.user.name}') # Вывести имя бота
	print(f'ID: {client.user.id}') # вывести id бота
	print(f'{Fore.GREEN}=========================') # Вывести зелёную строку

	a = randint(1,2) # Записываем в а рандомно 1 или 2 

	if a == 1: # Если а = 1
		await self.client.change_presence(status = discord.Status.online, activity = discord.Game(name = prefix + config.gaming))

		print("Bot playing!")
	else:
		await self.client.change_presence(status = discord.Status.online, activity = discord.Activity(name = config.invite, type = discord.ActivityType.listening))

		print("Bot listening invite!")

@bot.command() 
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
