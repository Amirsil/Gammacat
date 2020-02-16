import os
import json
import requests
import socket
from flask import Flask, render_template, url_for, request
import re
import sys
import webbrowser

app = Flask(__name__)
DB_NAME = 'db.txt'


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


@app.route('/', methods=['POST'])
def home():
    jdb = ''
    req = request.form
    if 'filename' not in req.keys():
        return ''
    filename = req['filename']

    if not filename:
        return json.dumps([])

    while not jdb:
        jdb = open(DB_NAME, 'r').read()

    if jdb and json.loads(jdb):
        db = json.loads(jdb)
    else:
        return json.dumps([])
    pass

    paths = []
    for path in db:
        file = re.search('([^\\\]+$)', path).group()
        if '.' in file:
            if filename in re.search(r'.*(?=\.)', file).group():
                paths.append((path, get_ip()))
        else:
            if filename in file:
                paths.append((path, get_ip()))
    return json.dumps(paths)


@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Node shutting down...'


def main():
    if not os.path.isfile('db.txt'):
        f = open('db.txt', 'w+')
        f.write(json.dumps([]))
        f.close()
    server_ip = sys.argv[1]
    print('''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
Connecting to server...
''')
    while True:
        try:
            r = requests.post("http://%s:5555/handle_new_connections" % server_ip, data={"ip": get_ip()})
            r = r
        except requests.exceptions.ConnectionError:
            continue
        break


if __name__ == '__main__':
    main()
