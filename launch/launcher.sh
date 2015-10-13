#!/bin/bash

. ~/.bashrc
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"

cd ~/dev/ATP/atp

#echo "`date +'%Y-%m-%d %H:%M:%S'`" >> tmp.log

python startWork.py ../casperjs/qunar.js
