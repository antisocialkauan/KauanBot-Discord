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
    await client.change_presence(game = discord.Game(name = 'test'), status = discord.Status('online'))

@client.event
async def on_message(message):
	userID = message.author.id

	if message.content.upper().startswith('PING'):
		game = message.content[6:]
		await client.change_presence(game=discord.Game(name=game))
		await client.send_message(message.channel, "Ich habe meinen Status zu " + game + " geaendert")

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
				teamicon = t_table[2]
				print('icon link: ', teamicon)
				print('standing: ', standing)
				print('team name: ', teamname)
				embed = discord.Embed(
					title = f'{teamname}',
					color = 0xffffff
					)
				embed.set_thumbnail(
					url = teamicon
					)
				embed.add_field(
					name = 'Standing',
					value = f'{standing}'
				)
				embed.set_footer(
					text = teamname,
					icon_url = teamicon
				)
				await client.send_message(message.channel, embed = embed)

    
	if message.content.upper().startswith(';CLEAR'):
			await client.purge_from(message.channel)



client.run('NDEzMTczNDk0MTQ3MTg2Njg4.DoaX-w.03EgKK1FuiX6v72r7uV9qjCNO1o')
