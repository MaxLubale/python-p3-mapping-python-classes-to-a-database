from config import CONN, CURSOR
from song import Song

if __name__ == '__main__':
    try:
        # Create the 'songs' table if it doesn't exist
        Song.create_table()

        # Create and save some songs
        hello = Song.create("Hello", "25")
        despacito = Song.create("Despacito", "Vida")

        # Access the IDs of the saved songs
        print(hello.id)
        print(despacito.id)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Commit changes and close the connection
        CONN.commit()
        CONN.close()

