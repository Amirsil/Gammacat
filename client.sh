#!/bin/bash
touch db.txt
pip install flask
pip install requests
echo 'Connecting to server...'
python Client.py
export FLASK_APP='Client.py'
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000
flask run
