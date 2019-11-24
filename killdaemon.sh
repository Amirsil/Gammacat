#!/bin/bash
python3 killdaemon.py
ps awx | grep daemon.py | grep -v "grep daemon.py" | awk '{print $1}' | xargs kill
