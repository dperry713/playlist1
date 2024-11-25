from flask import Blueprint, request, jsonify
from models.song import Song
from schema.song_schema import SongSchema

songs = []  # In-memory data store for songs
song_api = Blueprint('song_api', __name__)

@song_api.route('/', methods=['POST'])
def create_song():
    data = request.json
    try:
        SongSchema.validate(data)
        song = Song(**data)
        songs.append(song)
        return jsonify(song.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@song_api.route('/<int:song_id>', methods=['GET'])
def get_song(song_id):
    song = next((s for s in songs if s.song_id == song_id), None)
    if song:
        return jsonify(song.to_dict()), 200
    return jsonify({"error": "Song not found"}), 404

@song_api.route('/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    data = request.json
    song = next((s for s in songs if s.song_id == song_id), None)
    if song:
        song.name = data.get('name', song.name)
        song.artist = data.get('artist', song.artist)
        song.genre = data.get('genre', song.genre)
        return jsonify(song.to_dict()), 200
    return jsonify({"error": "Song not found"}), 404

@song_api.route('/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    global songs
    songs = [s for s in songs if s.song_id != song_id]
    return jsonify({"message": "Song deleted"}), 200
