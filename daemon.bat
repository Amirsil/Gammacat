start
type nul > daemon.txt
icacls db.txt /reset /t /c /q
python daemon.py