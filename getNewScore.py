
def get_team_stats_table(url):
	from BeautifulSoup import BeautifulSoup
	from urllib2 import urlopen
	return BeautifulSoup(urlopen(url).read()).find("table", "responsive").tbody


def is_hash_value_changed(oldValue, url):
	return oldValue != store_value(str(hash(str(get_team_stats_table(url)))))


FILENAME_FOR_STORAGE = ".tv2-tourmanager-hash-value"
def store_value(value):
	import sys,os
	open(os.path.dirname(sys.argv[0])+"/"+FILENAME_FOR_STORAGE, "w").write(value)
	return value

def read_old_value():
	import sys,os
	return open(os.path.dirname(sys.argv[0])+"/"+FILENAME_FOR_STORAGE, "r").read()

if __name__=="__main__":
	print is_hash_value_changed(read_old_value(), "http://tourmanager.tv2.no/stats/?view=con&year=CUR")