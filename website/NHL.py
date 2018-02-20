from bs4 import BeautifulSoup
from urllib.request import urlopen

nhl_teams = {
	'BLACKHAWKS' : 'chi/chicago-blackhawks',
	'AVALANCHE' : 'col/colorado-avalanche',
	'STARS' : 'dal/dallas-stars',
	'WILD' : 'min/minnesota-wild',
	'PREDATORS' : 'nsh/nashville-predators',
	'BLUES' : 'name/stl/st-louis-blues',
	'JETS' : 'name/wpg/winnipeg-jets',
	'DUCKS' : 'ana/anaheim-ducks',
	'COYOTES' : 'ari/arizona-coyotes',
	'FLAMES' : 'cgy/calgary-flames',
	'OILERS' : 'edm/edmonton-oilers',
	'KINGS' : 'la/los-angeles-kings',
	'SHARKS' : 'sj/san-jose-sharks',
	'CANUCKS' : 'van/vancouver-canucks',
	'GOLDEN KNIGHTS' : 'vgs/vegas-golden-knights',
	'BRUINS' : 'bos/boston-bruins',
	'SABRES' : 'buf/buffalo-sabres',
	'RED WINGS' : 'det/detroit-red-wings',
	'PANTHERS' : 'fla/florida-panthers',
	'CANADIENS' : 'mtl/montreal-canadiens',
	'SENATORS' : 'ott/ottawa-senators',
	'LIGHTNING' : 'tb/tampa-bay-lightning',
	'MAPLE LEAFS' : 'tor/toronto-maple-leafs',
	'HURRICANES' : 'car/carolina-hurricanes',
	'BLUE JACKETS' : 'cbj/columbus-blue-jackets',
	'DEVILS' : 'nj/new-jersey-devils',
	'ISLANDERS' : 'nyi/new-york-islanders',
	'RANGERS' : 'nyr/new-york-rangers',
	'FLYERS' : 'phi/philadelphia-flyers',
	'PENGUINS' : 'pit/pittsburgh-penguins',
	'CAPITALS' : 'wsh/washington-capitals'
}


def findStanding(team):
	url = link
	page = urlopen(url)
	soup = BeautifulSoup(page.read(), 'lxml')
	standings = soup.find('div', {'class': 'sub-title'}).contents
	standing = ' '.join(standings)
	print(standing)
	return standing

def findTeamName(link):
	url = link
	page = urlopen(url)
	soup = BeautifulSoup(page.read(), 'lxml')
	teamname = soup.find('div', {'id': 'sub-branding'}).h1.a.b.contents
	name = ' '.join(teamname)
	print(name)
	return name


findTeamName('http://www.espn.com/nhl/team/_/name/edm/edmonton-oilers')