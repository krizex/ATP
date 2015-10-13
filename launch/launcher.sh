#!/bin/bash

. ~/.bashrc
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"

cd ~/dev/ATP

#echo "`date +'%Y-%m-%d %H:%M:%S'`" >> tmp.log

python atp/startWork.py ../casperjs/qunar.js >> launch/run.log 2>&1
