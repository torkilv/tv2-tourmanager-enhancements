# tv2-tourmanager-enhancements
Simple scripts for getting enhanced info from tv2 tourmanager 2015 like sorting of best riders etc.

## getRiderStats.py
Usage: python getRiderStats.py [number of riders to pick]
getRiderStats fetches the statistis page from tv2 tourmanager, parses the rider info and outputs the top X in each category based on their cumulated points/price

## checkForNewScore.py
Checks whether the scores are updated since last time is run, based on score stored in .tv2-tourmanager-hash-value

May be used in conjunction with tv2-update-checker.sh which uses apple notifications to notify if there is a new score update, which should be used together with crontab for background checking
