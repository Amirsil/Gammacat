import subprocess
import time
while 1:
    time.sleep(0.1)
    if open('db.txt', 'r').read():
        break
