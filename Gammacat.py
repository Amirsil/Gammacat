import sys
import webbrowser
import subprocess
import os


def main():
    if len(sys.argv) > 1:

        if sys.argv[1] == '--version':
            print('''
gammacat (GNU coreutils) 1.0
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjorn Granlund and Richard M. Stallman. ''')
        elif sys.argv[1] in ['-d', '--daemon']:
            if os.path.isfile('daemon.txt'):
                print('''    
A daemon is already running in the background ''')
            else:
                print('''    
Starting daemon... ''')
                subprocess.call("daemon.bat")

        elif sys.argv[1] in ['-k', '--kill-daemon']:
            if not os.path.isfile('daemon.txt'):
                print('''             
No daemon is currently running ''')
            else:
                print('''          
Stopping daemon... ''')

                subprocess.call("killdaemon.sh", shell=True)

        elif sys.argv[1] in ['-s', '--server']:
            subprocess.call("server.bat")

        elif sys.argv[1] in ['-cs', '--close-server']:
            subprocess.call("killserver.sh", shell=True)
            while not os.path.isfile('deadserver'):
                pass
            if open('deadserver', 'r').read() == '\n':
                print('''                                       
No server is active on your computer right now ''')
            else:
                print(''' 
Server shutting down... ''')
            os.remove('deadserver')

        elif sys.argv[1] in ['-cn', '--close-node']:
            subprocess.call("killclient.sh", shell=True)
            while not os.path.isfile('deadclient'):
                pass
            if open('deadclient', 'r').read() == '\n':
                print('''                                       
No node is active on your computer right now ''')
            else:
                print(''' 
Node shutting down... ''')
            os.remove('deadclient')

        elif len(sys.argv) == 2:

            if sys.argv[1] in ['-c', '--connect']:
                print('''
usage: gammacat [-c, --connect] [HOST] ''')

            elif sys.argv[1] in ['-e', '--search']:
                print('''
usage: gammacat [-e, --search] [HOST] ''')

            else:
                print('''
usage: gammacat [OPTION] [HOST] ''')

        elif len(sys.argv) == 3:

            if sys.argv[1] in ['-c', '--connect']:
                subprocess.call(["client.bat", sys.argv[2]])

            elif sys.argv[1] in ['-e', '--search']:
                webbrowser.open_new_tab('http://%s:5555' % sys.argv[2])

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
        -k, --kill-daemon       stops the daemon that appends files from your computer to a local database
        -cs, --close-server     close the gammacat web main server that is open on your host
        -cn, --close-node       close the storage node that is connected to the main server
        --version               output version information and exits ''')


if __name__ == '__main__':
    main()
