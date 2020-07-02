start
python3 Node.py %1
export 'FLASK_APP'=Node.py
export 'FLASK_RUN_HOST'=0.0.0.0
export 'FLASK_RUN_PORT'=5550
flask run