start
python Node.py %1
set FLASK_APP=Node.py
set FLASK_RUN_HOST=0.0.0.0
set FLASK_RUN_PORT=5550
flask run