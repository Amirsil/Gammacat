from sys import argv
import webbrowser
import subprocess
import os
import requests


def main():
    if len(argv) > 1:

        if argv[1] == '--version':
            print('''
gammacat (GNU coreutils) 1.0
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjorn Granlund and Richard M. Stallman. ''')
        elif argv[1] in ['-d', '--daemon']:
            if os.path.isfile('daemon.txt'):
                print('''    
A daemon is already running in the background ''')
            else:
                print('''    
Starting daemon... ''')
                subprocess.call("daemon.bat")

        elif argv[1] in ['-k', '--kill-daemon']:
            if not os.path.isfile('daemon.txt'):
                print('''             
No daemon is currently running ''')
            else:
                print('''          
Stopping daemon... ''')

                subprocess.call("killdaemon.bat")

        elif argv[1] in ['-s', '--server']:
            try:
                requests.post("http://localhost:5555", timeout=0.1)
                print('''
A node is already active''')
            except requests.exceptions.ConnectionError:
                subprocess.call("server.bat")

        elif len(argv) == 2:

            if argv[1] in ['-c', '--connect']:
                print('''
usage: gammacat [-c, --connect] [HOST] ''')

            elif argv[1] in ['-e', '--search']:
                print('''
usage: gammacat [-e, --search] [HOST] ''')

            elif argv[1] in ['-cs', '--close-server']:
                try:
                    r = requests.post("http://localhost:5555/shutdown", timeout=0.1)
                    print(r.text)

                except requests.exceptions.ConnectionError:
                    print('''                                       
No server is active on your computer right now ''')

            elif argv[1] in ['-cn', '--close-node']:
                try:
                    r = requests.post("http://localhost:5550/shutdown", timeout=0.1)
                    print(r.text)

                except requests.exceptions.ConnectionError:
                    print('''                                       
No node is active on your computer right now ''')
            
            else:
                print('''
usage: gammacat [OPTION] [HOST] ''')

        elif len(argv) == 3:

            if argv[1] in ['-c', '--connect']:
                try:
                    r = requests.post("http://localhost:5550", timeout=0.1)
                    if r:
                        print('''
A server is already active''')
                except requests.exceptions.ConnectionError:
                    subprocess.call(["client.bat", argv[2]])

            elif argv[1] in ['-e', '--search']:
                try:
                    requests.post("http://%s:5555" % argv[2], timeout=0.1)
                    webbrowser.open_new_tab('http://%s:5555' % argv[2])
                except requests.exceptions.ConnectionError:
                    print('''
No server is active on this host                    
''')

            else:
                print('''
usage: gammacat [OPTION] [HOST] ''')

        else:
            print('''
usage: gammacat [OPTION] [HOST] ''')

    else:
        print('''
usage: gammacat [OPTION]
Software sollution for file search in a network of computers all connected to 1 main server.

        -s, --server            open the gammacat web main server on your host
        -c, --connect           connect to the server as a storage node
        -e, --search            connect to the main server from the browser to search files
        -d, --daemon            start a daemon that appends every file on your computer to a local database
        -k, --kill-daemon       stop the daemon that appends files from your computer to a local database
        -cs, --close-server     close the gammacat web main server that is open on your host
        -cn, --close-node       close the storage node that is connected to the main server
        --version               output version information and exits ''')


if __name__ == '__main__':
    main()
