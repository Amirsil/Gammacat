#!/bin/bash
pip install flask
pip install requests
python Client.py $1
export FLASK_APP='Client.py'
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000
flask run
