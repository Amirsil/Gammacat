import sys
import webbrowser
import subprocess
import os
import socket


## ip = socket.gethostbyname(socket.gethostname())


def main():
    if len(sys.argv) > 1:

        if sys.argv[1] == '--version':
            print('''
gammacat (GNU coreutils) 1.0
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjorn Granlund and Richard M. Stallman.
''')
        elif sys.argv[1] in ['-d', '--daemon']:
            if open('daemon.txt', 'r').read():
                print('A daemon is already running in the background')
            else:
                print('Starting daemon...')
                subprocess.call("daemon.sh", shell=True)

        elif sys.argv[1] in ['-k', '--kill-daemon']:
            print('Stopping daemon...')

            subprocess.call("killdaemon.sh", shell=True)

        elif sys.argv[1] in ['-s', '--server']:
            subprocess.call("server.sh", shell=True)

        elif len(sys.argv) == 2:

            if sys.argv[1] in ['-c', '--connect']:
                print('''
usage: gammacat [-c, --connect] [HOST]
            ''')

            elif sys.argv[1] in ['-e', '--search']:
                print('''
usage: gammacat [-e, --search] [HOST]
            ''')

        elif len(sys.argv) == 3:

            if sys.argv[1] in ['-c', '--connect']:
                subprocess.call("client.sh", shell=True)

            elif sys.argv[1] in ['-e', '--search']:
                webbrowser.open_new_tab('http://%s:5555' % sys.argv[2])

            else:
                print('''
usage: gammacat [OPTiON] [HOST]        

                ''')

        else:
            print('''
usage: gammacat [OPTION] [HOST]            

            ''')
    else:
        print('''
usage: gammacat [OPTION]
Software sollution for file search.

        -s, --server        open the gammacat web server on your local host
        -c, --connect       connect to the server as a storage node
        -e, --search        connect to the server as a client
        -d, --daemon        start a daemon that appends every file on your                                   computer to a local database
        -k, --kill-daemon   stops the daemon that appends files from your                                   computer to a local database
        --version           output version information and exits
                            ''')


if __name__ == '__main__':
    main()
