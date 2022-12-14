#!/usr/bin/python3
'''lists all states with a name starting with N (upper N)'''

import MySQLdb
import sys


def listAll():
    '''lists all states with a name that starts with N'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name regexp "^N.*" ' +
                'ORDER BY states.id ASC')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            if row[1][0] == "N":
                print(row)


if __name__ == "__main__":
    listAll()
