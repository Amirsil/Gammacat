pip install flask
pip install requests
python Client.py %1
set FLASK_APP=Client.py
set FLASK_RUN_HOST=0.0.0.0
set FLASK_RUN_PORT=5550
flask run
