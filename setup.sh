#!/bin/bash
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate
python3 setup.py install