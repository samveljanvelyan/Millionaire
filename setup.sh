#!/bin/bash

# Install Python 3.6 distribution.
sudo apt-get update
sudo apt-get install python3.6

# Install pip for our Python 3.6 version.
sudo apt-get install -y python3-pip

# Install virtual environment.
sudo apt-get install -y python3-venv

# Create virtual environment.
python3 -m venv venv

# Activate virtual environment.
source ./venv/bin/activate

# Installing project requirements.
pip install -r requirements.txt

# Navigate to projects folder.
cd ./Millionaire/

# Applying models migrations and migrating to the database.
python3 manage.py makemigrations
python3 manage.py migrate

# Filling the database with questions stored in "questions.txt".
python3 database_connector.py