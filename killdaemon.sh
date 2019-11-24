#!/bin/bash
ps aux | grep pty4 | awk '{print $1}' > daemon.txt
python killdaemon.py
ps aux | grep pty4 | awk '{print $1}' | xargs kill
rm daemon.txt
touch daemon.txt
