start
del db.txt
type nul > db.txt
ICACLS "db.txt" /grant "Users":F
type nul > daemon.txt
python daemon.py