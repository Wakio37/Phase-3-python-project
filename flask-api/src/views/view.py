from .config import CONN, CURSOR


class Actions:
    @staticmethod
    def search(search_term):
        sql = f'''
        WITH m AS (
            SELECT * FROM music
            WHERE name LIKE '{search_term}' OR artist LIKE '{search_term}' OR album LIKE '{search_term}'
        )
        SELECT json_group_array(
            json_object(
            'id', id, 
            'name', name, 
            'artist', artist, 
            'album', album, 
            'duration', duration)
            ) FROM m
        '''
        music = CURSOR.execute(sql).fetchall()
        return music

    @staticmethod
    def add_playlist(name, artist, album, duration):
        sql=f'''
        INSERT INTO playlist (name, artist, album, duration)
        VALUES (?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (name, artist, album, duration))
        CONN.commit()
        return Actions.playlist()

    @staticmethod
    def playlist():
        sql = '''
        SELECT json_group_array(
            json_object(
            'id', id, 
            'name', name, 
            'artist', artist, 
            'album', album, 
            'duration', duration)
            ) FROM playlist
        '''
        playlist = CURSOR.execute(sql).fetchall()
        return playlist

    @staticmethod
    def remove_playlist(id):
        sql = f'''
        DELETE FROM playlist
        WHERE id = {id}
        '''
        CURSOR.execute(sql)
        CONN.commit()
        return Actions.playlist()



