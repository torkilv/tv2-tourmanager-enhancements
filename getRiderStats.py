
#FETCHING AND PARSING (ADAPTER)
def get_rider_tableRows(url):
	from BeautifulSoup import BeautifulSoup
	from urllib2 import urlopen
	return BeautifulSoup(urlopen(url).read()).find("table", "responsive").tbody.findAll('tr')

def create_rider_dict_from_tablerow(riderTableRow):
	rider = {}
	values = riderTableRow.findAll('td');
	rider["name"] = values[0].a.text
	rider["team"] = values[1].text
	rider["category"] = values[2].text
	rider["value"] = float(values[3].text)
	rider["sprintrank"] = float(values[4].text)
	rider["climbrank"] = float(values[5].text)
	rider["rank"] = int(values[6].text)
	rider["lastStage"] = float(values[7].text)
	rider["chosenBy"] = values[8].text
	rider["totalPoints"] = float(values[9].text)
	return rider

def map_from_tableRow_to_rider(riderTableRows):
	return map(create_rider_dict_from_tablerow, riderTableRows)

def fetch_riders(url):
	return map_from_tableRow_to_rider(get_rider_tableRows(url))

#DATASTORE AND CALCULATIONS (MODEL)
def get_most_efficient_rank(rider):
	return -1 * rider["totalPoints"]/rider["value"]

def get_top_by_rank(riders, n):
	return sorted(riders, key=get_most_efficient_rank)[:n]

def filter_riders_by_type(riders, riderType):
	return filter(lambda rider: rider["category"] == riderType,riders)

def get_category_set(riders):
	return set(map(lambda rider: rider["category"], riders))

def get_top_by_type(riders, riderType, n):
	return get_top_by_rank(filter_riders_by_type(riders, riderType), n)


#PRINTING (VIEW)
def pretty_print_rider(rider):
	print rider["name"][:15] + "\t%g\t%g\t%g" % (rider["totalPoints"],rider["value"], -1 * get_most_efficient_rank(rider));

def pretty_print(riders):
	print "==== %g beste %s ====" % (len(riders), riders[0]["category"])
	print "Name\tTotal points\tValue\tEfficiency"
	map(pretty_print_rider, riders)
	print ""

def print_top_by_type(riders, riderType, n):
	pretty_print(get_top_by_type(riders, riderType, n))

def print_top_riders_for_all_categories(riders, n):
	map(lambda category: print_top_by_type(riders, category, n), get_category_set(riders))

if __name__=="__main__":
	import sys
	if len(sys.argv) < 2:
		print "Usage: python %s [number of riders to list]" % sys.argv[0]
		sys.exit(1)
	print_top_riders_for_all_categories(fetch_riders("http://tourmanager.tv2.no/stats/?view=drv&year=CUR"), int(sys.argv[1]))