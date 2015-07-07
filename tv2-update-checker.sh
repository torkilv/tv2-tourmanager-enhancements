#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
output=$(python $DIR/getNewScore.py)

truePythonString="True"
if [ $output=truePythonString ];
then
	/usr/bin/osascript -e 'display notification "Nye poeng delt ut" with title "TV2 Tourmanager"'
fi