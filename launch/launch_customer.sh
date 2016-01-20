#!/bin/bash

. ~/.bashrc
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"

cd ~/dev/ATP

python -m atp.custom.start_custom_work casperjs/qunar.js > /dev/null 2>>launch/err_custom.log 
