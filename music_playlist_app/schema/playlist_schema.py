class PlaylistSchema:
    @staticmethod
    def validate(data):
        required_fields = ['playlist_id', 'name']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing field: {field}")
