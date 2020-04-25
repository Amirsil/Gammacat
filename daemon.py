import json
import os
import time
import subprocess
DB_NAME = 'db.txt'


def main():
    if not os.path.isfile('db.txt'):
        f = open('db.txt', 'w+')
        f.write(json.dumps([]))
        f.close()
    _break = 0
    print('''
Close this daemon only from the command line using the -k option ''')
    try:
        while 1:
            if _break:
                break

            paths = []
            try:
                jdb = open(DB_NAME, 'r').read()
            except:
                jdb = json.dumps([])
                main()
            if jdb and json.loads(jdb):
                db = json.loads(jdb)
            else:
                db = []

            for root, directories, filenames in os.walk('C:/Users'):

                filenames = [f for f in filenames if not f[0] == '.']
                directories[:] = [d for d in directories if not d[0] == '.' and "AppData" not in d]

                if "AppData" in directories:
                    directories.remove("AppData")

                if os.path.isfile('killdaemon.txt'):
                    subprocess.call("del-killdaemon.bat")
                    time.sleep(0.1)
                    _break = 1

                if _break:
                    break

                for filename in filenames:
                    if _break:
                        break

                    path = os.path.join(root, filename)
                    paths.append(path)

                    if path in db:
                        continue

                    db.append(path)
                    jdb = json.dumps(db)
                    open(DB_NAME, 'w').write(jdb)

            while len(db) != len(paths):
                if os.path.isfile('killdaemon.txt'):
                    subprocess.call("del-killdaemon.bat")
                    time.sleep(0.1)
                    _break = 1
                    break

                if _break:
                    break

                for path in db:
                    if _break:
                        break

                    if path not in paths:
                        db.remove(path)
                        jdb = json.dumps(db)
                        open(DB_NAME, 'w').write(jdb)
    except:
        os.remove('daemon.txt')


if __name__ == "__main__":
    main()
