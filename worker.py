import discord
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ';')

@client.event
async def on_ready():
    print('Logged in as %s'  % client.user.name)
    

@client.event
async def on_message(message):
	if message.content.upper().startswith('PING'):
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Pong!" % (userID))
	if message.content.upper().startswith('SAY'):
		args = message.content.split(" ")
		await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
client.run('NDEzMTczNDk0MTQ3MTg2Njg4.DWlTeg.NPG4iTZiosEmhjhCtjvjVLBM9NE')