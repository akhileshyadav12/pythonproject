import sqlite3 as lite
import sys
con=None
try:
    con=lite.connect('test.db')
    cur=con.cursor()
    cur.execute('select sqlite_version()')
    data=cur.fetchone()
    print (data)
except lite.Error as e:
    print(e)
    sys.exit(1)
finally:
    if con:
        con.close()()
