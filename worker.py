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
    await client.edit_user(username = 'HockeyBot')
    

@client.event
async def on_message(message):
	userID = message.author.id
	if message.content.upper().startswith('PING'):
		await client.send_message(message.channel, "<@%s> Pong!" % (userID))
	if message.content.upper().startswith('SAY'):
		args = message.content.split(" ")
		await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
	if message.content.upper() == "HOCKEY":
		url = 'http://www.espn.com/nhl/team/_/name/la/los-angeles-kings'
		page = urlopen(url)
		soup = BeautifulSoup(page.read(), 'lxml')
		standings = soup.find('div', {'class': 'sub-title'}).contents
		wlt = ' '.join(standings)
		await client.send_message(message.channel, f'Stats (W/L/T) for Los Angeles Kings (LAK): {wlt} LINK: {url}')
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
				await client.send_message(message.channel, f'```\n'+
				f'	{teamname}	\n'+
				f'	{standing}	\n'+
				f'```')


client.run('NDEzMTczNDk0MTQ3MTg2Njg4.DWlTeg.NPG4iTZiosEmhjhCtjvjVLBM9NE')
