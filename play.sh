#!/bin/bash


rm -rf data
rm -f spectrum.log 
rm tests/test_data/main/wallet* 
killall /home/kim/src/specterext-taxtheft/.env/bin/python

pytest tests/test_playground.py
