import json
import os
import time
import subprocess
from getch import getch

DB_NAME = 'db.txt'
SEMAPHORE_NAME = 'daemon.txt'


def update_db():
    _break = 0
    try:
        while 1:
            if _break:
                break

            paths = []
            try:
                with open(DB_NAME, 'r') as f:
                    jdb = f.read()
                    f.close()
            except:
                jdb = json.dumps([])
                main()
            if jdb and json.loads(jdb):
                db = json.loads(jdb)
            else:
                db = []

            for root, directories, filenames in os.walk('/home'):

                filenames = [f for f in filenames if not f[0] == '.']
                directories[:] = [d for d in directories if not d[0] == '.' and "AppData" not in d]

                if "AppData" in directories:
                    directories.remove("AppData")

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
                    with open(DB_NAME, 'w') as f:
                        f.write(jdb)
                        f.close()

            while len(db) != len(paths):
                if _break:
                    break

                for path in db:
                    if path not in paths:
                        db.remove(path)
                        jdb = json.dumps(db)
                        with open(DB_NAME, 'w') as f:
                            f.write(jdb)
                            f.close()


    except:
        print('''
Process Closed''')
        os.remove(DB_NAME)
        os.remove(SEMAPHORE_NAME)


def main():
    with open(DB_NAME, 'w+') as f:
        f.write(json.dumps([]))
        f.close()
    open(SEMAPHORE_NAME, 'a').close()

    print('''
Press Ctrl + C in order to close this process ''')
    update_db()


if __name__ == "__main__":
    main()
