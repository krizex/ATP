#!/bin/bash

. ~/.bashrc
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"

cd ~/dev/ATP

#echo "`date +'%Y-%m-%d %H:%M:%S'`" >> tmp.log

python atp/start_work.py >> launch/run.log 2>&1
