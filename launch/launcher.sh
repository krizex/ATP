#!/bin/bash

. ~/.bashrc
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"

cd ~/dev/ATP

#echo "`date +'%Y-%m-%d %H:%M:%S'`" >> tmp.log

python -m atp.start_work >/dev/null 2>>launch/err.log 
