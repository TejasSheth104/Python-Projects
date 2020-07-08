# ask the user to enter 'Title', its 'Password' 
# and easily add it to the Database.
# 

import sqlite3
import getpass

conn = sqlite3.connect('SafeKeeper.sqlite')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS storePass(
        Title VARCHAR(100),
        Password VARCHAR(100),
        Security_QnA VARCHAR(100)
    )
    ''')

print('Enter your UserName and PassWord to store SAFELY.')
title = input('Enter the Title - ')
pswd = getpass.getpass('Enter the Password - ')
QnA = input('Enter the Security Answer(if any, 0 for NULL) - ')
if QnA == 0:
    QnA = 'NULL'

cur.execute('SELECT * FROM storePass')
for title_name in cur.fetchall():
    if title_name[0] == title:
        print('ALERT !\n\tThis TITLE Already EXISTS,')
        try:
            option = int(input('Would You LIke to UPDATE/DELETE this TITLE\n1.) UPDATE\n 2.) DELETE\nEnter - '))
            if 1 > option > 2:
                print('INVALID OPTION SELECTED, Default -> 1.')
                option = 1
        except TypeError:
            print('INVALID OPTION SELECTED, Default -> 1.')
            option = 1
        if option == 1:
            print('Enter the Password and/or Security Answer to Title - ', title)
            new_pswd = getpass.getpass('Enter the Password - ')
            new_QnA = input('Enter the Security Answer(if any, 0 for NULL) - ')
            if QnA == 0:
                QnA = 'NULL'
            
            cur.execute('''
                UPDATE storePass
                SET Password = (?, ),
                Security_QnA =  (?, )
                WHERE Title = (?, )''', 
                ((new_pswd, ), (new_QnA, ), (title_name[0], ))
            )      
        elif option == 2:
            sql_delete_query = '''DELETE FROM storePass WHERE Title LIKE ?'''
            cur.execute(sql_delete_query, (title_name[0], ))

cur.execute('''
    INSERT OR IGNORE INTO storePass(Title, Password, Security_QnA) VALUES (?, ?, ?)''', 
    (title, pswd, QnA)
)
conn.commit()

