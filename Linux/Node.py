import os
import json
import requests
import socket
from flask import Flask, render_template, url_for, request, send_file
import re
import sys
import webbrowser
from flask_cors import CORS, cross_origin
import urllib.parse

app = Flask(__name__)
app.config['SECRET_KEY'] = '0xdeadbeef'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/download_file": {"origins": "*"}})
DB_NAME = 'db.txt'


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


IP = get_ip()


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
        file = re.search('([^\/]+$)', path).group()
#        if '.' in file:
#            if filename.lower() in re.search(r'.*(?=\.)', file).group().lower()#                paths.append((path, IP))
        if filename == '.':
            paths.append((path, IP))
        elif filename.lower() in file.lower():
            paths.append((path, IP))
    return json.dumps(paths)


@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return '\nNode shutting down...'


@app.route('/download_file', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def download_file():
    req = request.args
    if 'path' not in request.args.keys():
        return ''
    path = request.args['path']
    print(path)
    try:
        return send_file(urllib.parse.unquote(path), as_attachment=True)
    except PermissionError:
        return "You don't have permission for this file!"


def main():
    if not os.path.isfile('db.txt'):
        f = open('db.txt', 'w+')
        f.write(json.dumps([]))
        f.close()
    server_ip = sys.argv[1]
    print('''
Connecting to server...''')
    while True:
        try:
            r = requests.post("http://%s:5555/handle_new_connections" % server_ip, data={"ip": IP})
            r = r
        except requests.exceptions.ConnectionError:
            continue
        break


if __name__ == '__main__':
    main()
