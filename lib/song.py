from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        with CONN:  # Use 'with' statement to manage the cursor
            CURSOR.execute(sql)
    
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        try:
            with CONN:
                CURSOR.execute(sql, (self.name, self.album))
                result = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()
                if result:
                    self.id = result[0]
        except Exception as e:
            print(f"Error in save method: {e}")

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
