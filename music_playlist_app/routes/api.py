from flask import Blueprint
from resources.song_resource import song_api
from resources.playlist_resource import playlist_api

api_blueprint = Blueprint('api', __name__)

# Register individual resource APIs
api_blueprint.register_blueprint(song_api, url_prefix='/songs')
api_blueprint.register_blueprint(playlist_api, url_prefix='/playlists')
