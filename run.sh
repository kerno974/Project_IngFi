#!/bin/bash

if [[ ! -d /main/.env ]]
then
    python3 -m venv .env  
    source .env/bin/activate
fi

source .env/bin/activate
python3 main.py
