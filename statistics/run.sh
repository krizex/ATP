#!/bin/bash

#export PYTHONPATH="../"

cd ..

python -m statistics.show_statistics FlightInfo $1
python -m statistics.show_statistics FlightLowestPriceInfo $1

