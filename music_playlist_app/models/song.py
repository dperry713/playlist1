class Song:
    def __init__(self, song_id, name, artist, genre):
        self.song_id = song_id
        self.name = name
        self.artist = artist
        self.genre = genre

    def to_dict(self):
        return {
            "song_id": self.song_id,
            "name": self.name,
            "artist": self.artist,
            "genre": self.genre,
        }
