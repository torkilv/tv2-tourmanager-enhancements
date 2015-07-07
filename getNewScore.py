
def get_tableRows(url):
	from BeautifulSoup import BeautifulSoup
	from urllib2 import urlopen
	return BeautifulSoup(urlopen(url).read()).find("table", "responsive").tbody.findAll('tr')

def is_sky_row(tableRow):
	return tableRow.findAll('td')[0].text == u'Team Sky'

def get_sky_overall_points_from_rows(tableRows):
	return store_sky_points(int(filter(is_sky_row, tableRows)[0].findAll('td')[6].text))

def is_sky_points_updated(oldScore, url):
	return oldScore > get_sky_overall_points_from_rows(get_tableRows(url))


FILENAME_FOR_STORAGE = ".tv2-tourmanager-sky-points-stored"
def store_sky_points(score):
	open(FILENAME_FOR_STORAGE, "w").write(str(score))
	return score

def read_old_sky_points():
	return int(open(FILENAME_FOR_STORAGE, "r").read())

if __name__=="__main__":
	print is_sky_points_updated(read_old_sky_points(), "http://tourmanager.tv2.no/stats/?view=con&year=CUR")