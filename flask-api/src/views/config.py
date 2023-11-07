import sqlite3

CONN = sqlite3.connect('music.db', check_same_thread=False)
CURSOR = CONN.cursor()

# create or replace table music
CURSOR.execute(
    '''
    CREATE TABLE IF NOT EXISTS music (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        artist TEXT,
        album TEXT,
        duration INTEGER
    );
    '''
)



CURSOR.execute(
    '''
    CREATE TABLE IF NOT EXISTS playlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        artist TEXT,
        album TEXT,
        duration INTEGER
    );
    '''
)

# CURSOR.execute(
#     '''
#     INSERT INTO music
#     (name, artist, album, duration)
#     VALUES 
#     ('Numb', 'Linkin Park', 'Hybrid Theory', 300)
#     '''
# )
# CONN.commit()