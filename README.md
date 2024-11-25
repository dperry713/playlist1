Music Playlist App
This is a Flask-based music playlist management application.

Features
Create, update, and delete songs and playlists.
Add or remove songs from playlists.
Sort songs within playlists by name, genre, or artist.
Setup
Clone the repository.
Create a virtual environment: python -m venv venv
Activate the virtual environment:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate
Install dependencies: pip install -r requirements.txt
Run the app: python app.py
API Endpoints
Refer to the source code for detailed endpoints.

Requirements
Flask==2.0.3
Werkzeug==2.0.3

## API Endpoints
1.1 Create a Song
Method: POST
URL: http://127.0.0.1:5000/api/songs/

1.2 Get a Song
Method: GET
URL: http://127.0.0.1:5000/api/songs/1

1.3 Update a Song
Method: PUT
URL: http://127.0.0.1:5000/api/songs/1

1.4 Delete a Song
Method: DELETE
URL: http://127.0.0.1:5000/api/songs/1

2.1 Create a Playlist
Method: POST
URL: http://127.0.0.1:5000/api/playlists/

2.2 Get a Playlist
Method: GET
URL: http://127.0.0.1:5000/api/playlists/1

2.3 Update a Playlist
Method: PUT
URL: http://127.0.0.1:5000/api/playlists/1

2.4 Delete a Playlist
Method: DELETE
URL: http://127.0.0.1:5000/api/playlists/1

3.1 Add a Song to a Playlist
Method: POST
URL: http://127.0.0.1:5000/api/playlists/1/add_song/1

Method: GET
URL: http://127.0.0.1:5000/api/playlists/1/sort?key=name

Replace key=name with:
key=artist to sort by artist.
key=genre to sort by genre.


