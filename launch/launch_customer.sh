#!/bin/bash

. ~/.bashrc
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"

cd ~/dev/ATP/launch
export PYTHONPATH="`pwd`/../atp"

python ../atp/custom/start_custom_work.py ../casperjs/qunar.js >> err.log 2>&1
