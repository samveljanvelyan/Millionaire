#!/bin/bash
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install -y python3-venv
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
cd ./Millionaire/
python3 manage.py makemigrations
python3 manage.py migrate
python3 database_connector.py