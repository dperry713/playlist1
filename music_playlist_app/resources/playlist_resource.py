from flask import Blueprint, request, jsonify
from models.playlist import Playlist
from models.song import Song
from schema.playlist_schema import PlaylistSchema
from resources.song_resource import songs

playlists = []  # In-memory data store for playlists
playlist_api = Blueprint('playlist_api', __name__)

@playlist_api.route('/', methods=['POST'])
def create_playlist():
    data = request.json
    try:
        PlaylistSchema.validate(data)
        playlist = Playlist(data['playlist_id'], data['name'])
        playlists.append(playlist)
        return jsonify(playlist.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@playlist_api.route('/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    playlist = next((p for p in playlists if p.playlist_id == playlist_id), None)
    if playlist:
        return jsonify(playlist.to_dict()), 200
    return jsonify({"error": "Playlist not found"}), 404

@playlist_api.route('/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    data = request.json
    playlist = next((p for p in playlists if p.playlist_id == playlist_id), None)
    if playlist:
        playlist.name = data.get('name', playlist.name)
        return jsonify(playlist.to_dict()), 200
    return jsonify({"error": "Playlist not found"}), 404

@playlist_api.route('/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    global playlists
    playlists = [p for p in playlists if p.playlist_id != playlist_id]
    return jsonify({"message": "Playlist deleted"}), 200

@playlist_api.route('/<int:playlist_id>/add_song/<int:song_id>', methods=['POST'])
def add_song_to_playlist(playlist_id, song_id):
    playlist = next((p for p in playlists if p.playlist_id == playlist_id), None)
    song = next((s for s in songs if s.song_id == song_id), None)
    if playlist and song:
        playlist.songs.append(song)
        return jsonify(playlist.to_dict()), 200
    return jsonify({"error": "Playlist or Song not found"}), 404

@playlist_api.route('/<int:playlist_id>/sort', methods=['GET'])
def sort_playlist(playlist_id):
    playlist = next((p for p in playlists if p.playlist_id == playlist_id), None)
    if playlist:
        sort_key = request.args.get('key', 'name')
        playlist.songs.sort(key=lambda x: getattr(x, sort_key))
        return jsonify(playlist.to_dict()), 200
    return jsonify({"error": "Playlist not found"}), 404
