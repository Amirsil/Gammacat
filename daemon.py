import json
import os
import time

DB_NAME = 'db.txt'


def main():
    print('Uploading files to local database')
    while 1:
        _break = 0
        added_paths = 0
        removed_paths = 0
        paths = []
        jdb = open(DB_NAME, 'r').read()
        if jdb and json.loads(jdb):
            db = json.loads(jdb)
        else:
            db = []

        for root, directories, filenames in os.walk('/'):
            for filename in filenames:

                path = os.path.join(root, filename)
                paths.append(path)

                if path in db:
                    continue

                db.append(path)
                jdb = json.dumps(db)
                f = open(DB_NAME, 'w')
                f.write(jdb)

        while len(db) != len(paths):
            for path in db:
                if path not in paths:
                    db.remove(path)
                    jdb = json.dumps(db)
                    f = open(DB_NAME, 'w')
                    f.write(jdb)



if __name__ == "__main__":
    main()
