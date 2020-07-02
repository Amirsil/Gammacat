#!/bin/sh
export 'FLASK_APP'=Server.py
export 'FLASK_RUN_PORT'=5555
export 'FLASK_RUN_HOST'=0.0.0.0
flask run
