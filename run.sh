#!/bin/bash

if [[ ! -d /main/.env ]]
then
    python3 -m venv .env  
    source .env/bin/activate
fi

source .env/bin/activate
pip3 install pandas
python3 main.py
