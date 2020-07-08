# ask the user to enter 'Title', its 'Password' 
# and easily add it to the Database.
# 

import sqlite3
import getpass

conn = sqlite3.connect('SafeKeeper.sqlite')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS storePass(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Title VARCHAR(100) UNIQUE,
        Password VARCHAR(100),
        Security_QnA VARCHAR(100)
    )
    ''')


def add_record():
    print('Enter your UserName and PassWord to store SAFELY.')
    title = input('Enter the Title - ')
    check(title)
    pswd = getpass.getpass('Enter the Password - ')
    QnA = input('Enter the Security Answer(if any, 0 for NULL) - ')
    if QnA == 0:
        QnA = 'NULL'

    cur.execute('''
        INSERT OR IGNORE INTO storePass(Title, Password, Security_QnA) VALUES (?, ?, ?)''', 
        (title, pswd, QnA)
    )
    conn.commit()


def view_record():
    print('View Record by -')
    try:
        select = int(input(' 1.) Title\n 2.) Security Question\nEnter - '))
    except TypeError:
        print('INVALID OPTION SELECTED, Default -> 1.')
        select = 1
    if 1 > select > 2:
        print('INVALID OPTION SELECTED, Default -> 1.')
        select = 1
    if select == 1:
        # view_by = 'Title'
        title = input('Enter the Title - ')
        view_type = title
        cur.execute('SELECT * FROM storePass WHERE Title = ?', (view_type))
        for row in cur.fetchall():
            print(row)
    elif select == 2:
        # view_by = 'Security_QnA'
        QnA = input('Enter the Security Answer(if any, 0 for NULL) - ')
        if QnA == 0:
            QnA = 'NULL'
        view_type = QnA
        cur.execute('SELECT * FROM storePass WHERE Security_QnA = ?', (view_type))
        for row in cur.fetchall():
            print(row)


def check(title):
    cur.execute('SELECT * FROM storePass')
    for title_name in cur.fetchall():
        if title_name[0] == title:
            print('ALERT !\n\tThis TITLE Already EXISTS,')
            try:
                option = int(input('Would You LIke to UPDATE/DELETE this TITLE\n1.) UPDATE\n 2.) DELETE\nEnter - '))
            except TypeError:
                print('INVALID OPTION SELECTED, Default -> 1.')
                option = 1
            if 1 > option > 2:
                print('INVALID OPTION SELECTED, Default -> 1.')
                option = 1
            sql_delete_query = '''DELETE FROM storePass WHERE Title LIKE ?'''
            cur.execute(sql_delete_query, (title_name[0], ))
            if option == 1:
                print('Enter the Password and/or Security Answer to Title - ', title)
                new_pswd = getpass.getpass('Enter the Password - ')
                new_QnA = input('Enter the Security Answer(if any, 0 for NULL) - ')
                if QnA == 0:
                    QnA = 'NULL'
            
                data = (new_pswd, new_QnA, title_name[0])
                cur.execute('''
                    UPDATE storePass
                    SET Password = ?,
                    Security_QnA =  ?
                    WHERE Title = ?''', 
                    data
                )


print('WELCOME - ')
print('What do you want to do?')
try:
    select = int(input(' 1.) ADD NEW.\n 2.) VIEW EXISTING.\nEnter - '))
except TypeError:
    print('INVALID OPTION SELECTED, Default -> 1.')
    select = 1
if 1 > select > 2:
    print('INVALID OPTION SELECTED, Default -> 1.')
    select = 1
if select == 1:
    add_record()
elif select == 2:
    view_record()

print('THANK YOU...')
