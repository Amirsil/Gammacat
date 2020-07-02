from flask import Flask, render_template, url_for, request
import json
import requests
from datetime import datetime
import re
import time
import socket
import urllib.parse
app = Flask(__name__)
ip_list = []
my_ip = 'localhost'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/handle_new_connections', methods=['POST'])
def handle_new_connections():
    req = request.form
    if 'ip' not in req.keys():
        return 'Please specify the IP you want to connect with'
    ip = req['ip']
    if ip not in ip_list:
        ip_list.append(ip)
    return ''


@app.route('/handle_request', methods=['POST'])
def handle_request():
    if ip_list:
        paths = []
        req = request.form
        if 'filename' not in req.keys():
            return render_template('home.html', title='Home')
        filename = req['filename']
        for ip in ip_list:
            try:
                r = requests.post("http://%s:5550" % ip, data={"filename": filename}, timeout=3)
                r = r  # an operation on r must be done for some reason, else an exception occures.
                if r.text:
                    print(r.text)
                    paths += json.loads(r.text.replace('\\', '/').replace('\\\\', '/'))
            except:
                ip_list.remove(ip)
        print('Connected storage nodes:\n%s' % '%s\n' % ''.join([ip for ip in ip_list]))
        print(paths)
        filenames = [re.search(r'([^\/]+$)', path).group() for path, ip in paths]
        return render_template('home.html', title='Home', paths=paths, filenames=filenames)
    return render_template('home.html', title='Home')


@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return '\nServer shutting down...'


if __name__ == "__main__":
    app.run(debug=True)
