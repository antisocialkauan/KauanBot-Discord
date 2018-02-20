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

def findSite(dictionary, target):
	for key, val in dictionary.items():
		if key == target:
			return val

def findTeam(string):
	if string.upper() == 'BLACKHAWKS' or string.upper() == 'CHICAGO' or string.upper() == 'CHICAGO BLACKHAWKS':
		return findSite(nhl_teams, 'BLACKHAWKS')
	elif string.upper() == 'AVALANCHE' or string.upper() == 'COLORADO' or string.upper() == 'COLORADO AVALANCHE':
		return findSite(nhl_teams, 'AVALANCHE')
	elif string.upper() == 'STARS' or string.upper() == 'DALLAS' or string.upper() == 'DALLAS STARS':
		return findSite(nhl_teams, 'STARS')
	elif string.upper() == 'WILD' or string.upper() == 'WILD' or string.upper() == 'MINNESOTA WILD':
		return findSite(nhl_teams, 'WILD')
	elif string.upper() == 'PREDATORS' or string.upper() == 'NASHVILLE' or string.upper() == 'NASHVILLE PREDATORS':
		return findSite(nhl_teams, 'PREDATORS')
	elif string.upper() == 'BLUES' or string.upper() == 'ST. LOUIS' or string.upper() == 'ST. LOUIS' or string.upper() == 'ST LOUIS BLUES' or string.upper() == 'ST. LOUIS BLUES':
		return findSite(nhl_teams, 'BLUES')
	elif string.upper() == 'JETS' or string.upper() == 'WINNIPEG' or string.upper() == 'WINNIPEG JETS':
		return findSite(nhl_teams, 'JETS')
	elif string.upper() == 'DUCKS' or string.upper() == 'ANAHEIM' or string.upper() == 'ANAHEIM DUCKS':
		return findSite(nhl_teams, 'DUCKS')
	elif string.upper() == 'COYOTES' or string.upper() == 'ARIZONA' or string.upper() == 'ARIZONA COYOTES':
		return findSite(nhl_teams, 'COYOTES')
	elif string.upper() == 'FLAMES' or string.upper() == 'CALGARY' or string.upper() == 'CALGARY FLAMES':
		return findSite(nhl_teams, 'FLAMES')
	elif string.upper() == 'OILERS' or string.upper() == 'EDMONTON' or string.upper() == 'EDMONTON OILERS':
		return findSite(nhl_teams, 'OILERS')
	elif string.upper() == 'KINGS' or string.upper() == 'LOS ANGELES' or string.upper() == 'LA' or string.upper() == 'LOS ANGELES KINGS' or string.upp() == 'LA KINGS':
		return findSite(nhl_teams, 'KINGS')
	elif string.upper() == 'SHARKS' or string.upper() == 'SAN JOSE' or string.upper() == 'SAN JOSE SHARKS':
		return findSite(nhl_teams, 'SHARKS')
	elif string.upper() == 'CANUCKS' or string.upper() == 'VANCOUVER' or string.upper() == 'VANCOUVER CANUCKS':
		return findSite(nhl_teams, 'CANUCKS')
	elif string.upper() == 'GOLDEN KNIGHTS' or string.upper() == 'VEGAS' or string.upper() == 'VEGAS GOLDEN KNIGHTS':
		return findSite(nhl_teams, 'GOLDEN KNIGHTS')
	elif string.upper() == 'BRUINS' or string.upper() == 'BOSTON' or string.upper() == 'BOSTON BRUINS':
		return findSite(nhl_teams, 'BRUINS')
	elif string.upper() == 'SABRES' or string.upper() == 'BUFFALO' or string.upper() == 'BUFFALO SABRES':
		return findSite(nhl_teams, 'SABRES')
	elif string.upper() == 'RED WINGS' or string.upper() == 'DETROIT' or string.upper() == 'DETROIT RED WINGS':
		return findSite(nhl_teams, 'RED WINGS')
	elif string.upper() == 'PANTHERS' or string.upper() == 'FLORIDA' or string.upper() == 'FLORIDA PANTHERS':
		return findSite(nhl_teams, 'PANTHERS')
	elif string.upper() == 'CANADIENS' or string.upper() == 'MONTREAL' or string.upper() == 'MONTREAL CANADIENS':
		return findSite(nhl_teams, 'CANADIENS')
	elif string.upper() == 'SENATORS' or string.upper() == 'OTTAWA' or string.upper() == 'OTTAWA SENATORS':
		return findSite(nhl_teams, 'SENATORS')
	elif string.upper() == 'LIGHTNING' or string.upper() == 'TAMPA BAY' or string.upper() == 'TAMPA BAY LIGHTNING':
		return findSite(nhl_teams, 'LIGHTNING')
	elif string.upper() == 'MAPLE LEAFS' or string.upper() == 'TORONTO' or string.upper() == 'TORONTO MAPLE LEAFS':
		return findSite(nhl_teams, 'MAPLE LEAFS')
	elif string.upper() == 'HURRICANES' or string.upper() == 'CAROLINA' or string.upper() == 'CAROLINA HURRICANES':
		return findSite(nhl_teams, 'HURRICANES')
	elif string.upper() == 'BLUE JACKETS' or string.upper() == 'COLUMBUS' or string.upper() == 'COLUMBUS BLUE JACKETS':
		return findSite(nhl_teams, 'BLUE JACKETS')
	elif string.upper() == 'DEVILS' or string.upper() == 'NEW JERSEY' or string.upper() == 'NEW JERSEY DEVILS':
		return findSite(nhl_teams, 'DEVILS')
	elif string.upper() == 'ISLANDERS' or string.upper() == 'NEW YORK ISLANDERS':
		return findSite(nhl_teams, 'ISLANDERS')
	elif string.upper() == 'RANGERS' or string.upper() == 'NEW YORK RANGERS':
		return findSite(nhl_teams, 'RANGERS')
	elif string.upper() == 'FLYERS' or string.upper() == 'PHILADELPHIA' or string.upper() == 'PHILADELPHIA FLYERS':
		return findSite(nhl_teams, 'FLYERS')
	elif string.upper() == 'PENGUINS' or string.upper() == 'PITTSBURGH' or string.upper() == 'PITTSBURGH PENGUINS':
		return findSite(nhl_teams, 'PENGUINS')
	elif string.upper() == 'CAPITALS' or string.upper() == 'WASHINGTON' or string.upper() == 'WASHINGTON CAPITALS':
		return findSite(nhl_teams, 'CAPITALS')
	else:
		return 'NaT'

def getStanding(team):
	url = findTeam(team)
	page = urlopen(url)
	soup = BeautifulSoup(page.read(), 'lxml')
	teamstanding = soup.find('div', {'class': 'sub-title'}).contents
	return teamstanding
