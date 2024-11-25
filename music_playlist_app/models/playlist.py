class Playlist:
    def __init__(self, playlist_id, name, songs=None):
        self.playlist_id = playlist_id
        self.name = name
        self.songs = songs if songs else []

    def to_dict(self):
        return {
            "playlist_id": self.playlist_id,
            "name": self.name,
            "songs": [song.to_dict() for song in self.songs],
        }
