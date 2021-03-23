#!/bin/bash

if [[ ! -f /main/.env ]]
then
    python3 -m venv .env  
    source .env/bin/activate
    pip install -r requirements.txt
fi

source .env/bin/activate
python main.py
