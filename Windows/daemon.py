import json
import os
import time
import subprocess
from msvcrt import kbhit, getch

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

                if kbhit() and getch() == chr(27).encode():
                    time.sleep(0.1)
                    _break = 1
                    os.remove(DB_NAME)
                    os.remove(SEMAPHORE_NAME)
                    break

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
                if kbhit() and getch() == chr(27).encode():
                    time.sleep(0.1)
                    _break = 1
                    os.remove(DB_NAME)
                    os.remove(SEMAPHORE_NAME)
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

    except PermissionError:
        update_db()


def main():
    with open(DB_NAME, 'w+') as f:
        f.write(json.dumps([]))
        f.close()
    open(SEMAPHORE_NAME, 'a').close()

    print('''
Press Esc in order to close this process ''')
    update_db()


if __name__ == "__main__":
    main()
