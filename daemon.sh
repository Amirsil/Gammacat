#!/bin/bash
touch db.txt
python daemon.py&
ps aux | grep pty4 | awk '{print $1}' > daemon.txt
