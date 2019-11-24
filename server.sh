#!/bin/bash
pip3 install flask
pip3 install requests
export FLASK_APP='Server.py'
export FLASK_RUN_PORT=5555
export FLASK_DEBUG=1
export FLASK_RUN_HOST=0.0.0.0
flask run
