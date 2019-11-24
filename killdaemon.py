import subprocess
import time
while 1:
    if not open('deamon.txt', 'r').read():
        print('No daemon is currently running')
        break
    time.sleep(0.5)
    if open('db.txt', 'r').read():
        break
