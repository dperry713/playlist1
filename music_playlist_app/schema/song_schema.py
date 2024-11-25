class SongSchema:
    @staticmethod
    def validate(data):
        required_fields = ['song_id', 'name', 'artist', 'genre']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing field: {field}")
