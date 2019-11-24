#!/bin/bash
pip3 install flask
pip3 install requests
ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' > ip.txt
python3 Client.py
touch db.txt
export FLASK_APP='Client.py'
export FLASK_RUN_HOST=0.0.0.0
flask run
