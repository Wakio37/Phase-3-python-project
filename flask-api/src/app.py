import flask 
from views.view import Actions
from flask_cors import CORS
from flask import request
import json


app = flask.Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/songs", methods=["GET"])
def music_list():
    search_term = request.args.get('search')
    return Actions.search(search_term)

@app.route("/add_playlist", methods=["POST"])
def add_playlist():
    data = json.loads(request.data) #request.data
    name = data['name']
    artist = data['artist']
    album = data['album']
    duration = data['duration']
    return Actions.add_playlist(name, artist, album, duration)

@app.route("/playlist", methods=["GET"])
def playlist():
    return Actions.playlist()

@app.route("/remove_playlist", methods=["POST"])
def remove_playlist():
    data = request.data
    data = json.loads(data)
    id = data['id']

    return Actions.remove_playlist(id)