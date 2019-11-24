#!/bin/bash
pip install flask
pip install requests
python Client.py
export FLASK_APP='Client.py'
export FLASK_RUN_HOST=0.0.0.0
flask run
