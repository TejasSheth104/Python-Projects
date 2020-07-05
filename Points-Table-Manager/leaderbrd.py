import sqlite3

conn = sqlite3.connect('leaderboard.sqlite')
cur = conn.cursor()

# table named - Points_Table
cur.execute('''CREATE TABLE IF NOT EXISTS Points_Table \
            (Player_Name TEXT, Team_Name TEXT UNIQUE, \
            Wins INTEGER, Loss INTEGER, Draws INTEGER, \
            Points INTEGER, GF INTEGER, GA INTEGER, GD INTEGER, Records TEXT)''')
print('DATABASE Created .')

t_no_play = int(input('Enter Total Number of Players - '))
count = 0
# input for player_name and team_name
while count < t_no_play:
    p_name = str(input('Enter Player\'s Name - '))
    team_name = str(input('Enter Team Name - '))
    matches = int(input('Enter Matches Played - '))
    cur.execute('INSERT OR IGNORE INTO Points_Table (Player_Name, Team_Name) VALUES (?, ?)', (p_name, team_name))
    count += 1
    if p_name != '' and team_name != '':
        # cur.execute('INSERT OR IGNORE INTO Points_Table (Player_Name, Team_Name) VALUES (?, ?)', (p_name, team_name))
        increase, points, scored, conceded, difference = 0, 0, 0, 0, 0
        record = ''
        while increase < matches:
            print('Enter MatchDay', len(record) + 1, '- ')
            gf = int(input('Enter Goals Scored - '))
            ga = int(input('Enter Goals Conceded - '))
            if gf < 0 or ga < 0:
                count -= 1
                print('RETRY ...')
                continue
            gd = gf - ga
            scored += gf
            conceded += ga
            difference = scored - conceded
            #            print(gd)
            if gd > 0:      record = 'W' + record
            elif gd < 0:    record = 'L' + record
            elif gd == 0:   record = 'D' + record

            if record[0] == 'W':    points += 3
            elif record[0] == 'L':  points += 0
            elif record[0] == 'D':  points += 1
            gf = str(gf)
            ga = str(ga)
            # cur.execute('INSERT OR IGNORE INTO Points_Table (GF, GA, GD) VALUES (?, ?, ?)', (gf, ga, gd))
            increase += 1
            cur.execute('INSERT OR REPLACE INTO Points_Table \
                            (Player_Name, Team_Name, Wins, Loss, Draws, Points, GF, GA, GD, Points, Records) '
                        'VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                        (p_name, team_name, scored, conceded, difference, points, record))
            conn.commit()
cur.close()

s
