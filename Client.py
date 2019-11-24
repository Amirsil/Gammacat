import os
import json
import requests
import socket
from flask import Flask, render_template, url_for, request
import re
import sys


app = Flask(__name__)
ip = socket.gethostbyname(socket.gethostname())
DB_NAME = 'db.txt'


@app.route('/', methods=['POST'])
def home():
    jdb = ''
    req = request.form
    if 'filename' not in req.keys():
        return ''
    filename = req['filename']
    while not jdb:
        jdb = open(DB_NAME, 'r').read()

    if jdb and json.loads(jdb):
        db = json.loads(jdb)
    else:
        db = []
    pass

    paths = []
    for path in db:
        file = re.search('([^\\\]+$)', path).group()
        if '.' in file:
            if filename in re.search(r'.*(?=\.)', file).group():
                paths.append((path, ip))
        else:
            if filename in file:
                paths.append((path, ip))
    return json.dumps(paths)


def main():
    if len(sys.argv) > 1:
        server_ip = sys.argv[1]
    else:
        server_ip = 'localhost'
    if not os.path.isfile(DB_NAME):
        open(DB_NAME, 'w+')
    print('''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   Connecting to server...

''')
    while True:
        try:
            requests.post("http://%s:5555/handle_new_connections" % server_ip, data={"ip": ip}, timeout=0.1)
        except:
            continue
        break


if __name__ == '__main__':
    main()
