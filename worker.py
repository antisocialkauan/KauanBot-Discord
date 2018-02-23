import discord
from discord.ext import commands
import asyncio
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from website.nhl import getStanding

Client = discord.Client()
client = commands.Bot(command_prefix = ';')

@client.event
async def on_ready():
    print('Logged in as %s'  % client.user.name)
    

@client.event
async def on_message(message):
	userID = message.author.id
	if message.content.upper().startswith('PING'):
		await client.send_message(message.channel, "<@%s> Pong!" % (userID))
	if message.content.upper().startswith('SAY'):
		args = message.content.split(" ")
		await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
	if message.content.upper().startswith(';HOCKEY'):
		msg = message.content.split()
		print(msg)
		if len(msg) > 1:
			team = msg[1]
			print(team)
			t_table = getStanding(team)
			if t_table == 'NaT':
				await client.send_message(message.channel, f'<@{userID}> I couldn\'t detect any NHL team, make sure you typed it correctly. (EX. For the Carolina Hurricanes, you could type: Carolina, Hurricanes, or Carolina Hurricanes ' )
			else:
				standing = t_table[0]
				teamname = t_table[1]
				print('standing: ', standing)
				print('team name: ', teamname)
				embed = discord.Embed(
					title = f'{teamname}',
					color = 0xffffff
					)
				embed.add_field(
					name = f'Standing',
					value = f'{standing}'
				)
				embed.set_footer(
					text = 'Bot by h0ckey',
					icon_url = 'https://cdn.discordapp.com/avatars/213854012473212929/55641ca7fdb5ae17f64e97f5b984d0bd.png'
				)
				await client.send_message(message.channel, embed = embed)
	if message.content.upper().startswith(';CLEAR'):
		await client.purge_from(message.channel)


client.run('NDEzMTczNDk0MTQ3MTg2Njg4.DWlTeg.NPG4iTZiosEmhjhCtjvjVLBM9NE')
