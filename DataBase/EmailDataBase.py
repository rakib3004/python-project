import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

iEmail = 'stephen.marquard@uct.ac.za'

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'data'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('''SELECT count FROM Counts WHERE email = 'stephen.marquard@uct.ac.za' ''', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES ('stephen.marquard@uct.ac.za', 1)''', (email,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE email = 'stephen.marquard@uct.ac.za';''',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = '''SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'''

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()