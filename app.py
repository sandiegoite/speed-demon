import uuid

from flask import abort, Flask, jsonify, redirect, render_template, request, url_for
from flask_socketio import emit, join_room, leave_room, send, SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

ongoing_games = {}

class Game:
    def __init__(self, owner):
        self.id = uuid.uuid4()
        self.owner = owner
    def serialize(self):
        return {"id": self.id, "owner": self.owner}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/games/<game_id>')
def game(game_id):
    game_id = uuid.UUID(game_id)
    if game_id not in ongoing_games:
        abort(404)
    return render_template('game.html', game=ongoing_games[game_id])

@app.route('/api/games', methods=['GET'])
def games():
    return jsonify([game.serialize() for (game_id, game) in ongoing_games.items()])

@app.route('/api/games', methods=['POST'])
def new_game():
    game = Game(request.form['owner'])
    ongoing_games[game.id] = game
    return redirect(url_for('game', game_id=game.id))

@socketio.on('join')
def on_join(data):
    game = data['game']
    join_room(game)

@socketio.on('message')
def on_message(data):
    game = data['game']
    message = data['message']
    join_room(game)
    emit('message', {'message': message}, room=game)

if __name__ == '__main__':
    socketio.run(app)
