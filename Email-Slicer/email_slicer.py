# get the username and domain name,
# customize this to send a message to host with this information,
# create a database to store all user names, domain names, and email address
# eg.   tejassheth104@gmail.com  =>     tejassheth104,      gmail.com

import sqlite3
import ssl
import re
import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

unwanted = '<>;:/?()""'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('emailnet.sqlite')
cur = conn.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS username(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    u_name TEXT)''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS domain_name(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    dm_name TEXT UNIQUE)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS e_mail(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    address TEXT UNIQUE,
    user_id INTEGER,
    domain_id INTEGER)''')
#    url TEXT UNIQUE,
#    FOREIGN KEY (user_id) REFERENCES username(id),
#    FOREIGN KEY (domain_id) REFERENCES domain_name(id)
# , url

cur.execute('SELECT id, address FROM e_mail ORDER BY RANDOM() LIMIT 1')
row = cur.fetchone()
if row is not None:
    print("Restarting existing Analysis.  Remove emailnet.sqlite to start a fresh analysis.")
else:
    # eid = input('Enter your Email Id. - ')
    # pieces = eid.split('@')
    # print(pieces)
    starturl = input('Enter File Name or enter - ')
    if len(starturl) < 1:
        starturl = 'mbox.txt'
    if len(starturl) > 1:
        cur.execute('INSERT OR IGNORE INTO Webs(url) VALUES (?)', (starturl, ))
#        cur.execute('INSERT OR IGNORE INTO e_mail (address, url) VALUES (?, ?)', (eid , starturl))
        conn.commit()

cur.execute('SELECT url FROM Webs')
webs = list()
for row in cur:
    webs.append(str(row[0]))
print(webs)

count = 0
mails = list()
try:
    val = int(input('How many Emails - '))
except (TypeError, ValueError):
    print('Try Again..')
    exit(-1)

piece = ''
while True:
# , url
    cur.execute('SELECT id, address FROM e_mail ORDER BY RANDOM() LIMIT 1')
    row = cur.fetchone()
    fhandle = open(webs[0])
    for line in fhandle:
        count += 1
        line = line.strip()
        mail = re.findall('\S+@\S+', line)
        if len(mail) > 0:
            piece = str(mail[0])
            for letters in piece:
                if letters in unwanted:
                    piece = piece.strip(unwanted)
            if len(mail) < 0:
                break
        print(piece)
        pieces = piece.split('@')
#                mails.append(piece)

        print('Count of Emails - ', count,)
#    cur.execute('SELECT id, address FROM e_mail ORDER BY RANDOM() LIMIT 1')
#    row = cur.fetchone()
#    for mailid in mails:

        print(pieces)
        cur.execute('''INSERT OR REPLACE INTO username (u_name) 
            VALUES (?)''', (pieces[0], ))
        cur.execute('SELECT id FROM username WHERE u_name = ?', (pieces[0], ))
        user_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO domain_name (dm_name)
            VALUES (?)''', (pieces[1], ))
        cur.execute('SELECT id FROM domain_name WHERE dm_name = ?', (pieces[1], ))
        domain_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO e_mail (address, user_id, domain_id)
            VALUES (?, ?, ?)''', (piece, user_id, domain_id))

        conn.commit()