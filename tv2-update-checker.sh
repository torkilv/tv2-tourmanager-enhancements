#!/bin/bash
output=$(python getNewScore.py)

truePythonString="True"
if [ $output=truePythonString ];
then
	/usr/bin/osascript -e 'display notification "Nye poeng delt ut" with title "TV2 Tourmanager"'
fi