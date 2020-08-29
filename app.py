import uuid

from flask import Flask, jsonify, render_template
app = Flask(__name__)

class Game:
    def __init__(self):
        self.id = uuid.uuid4()
    def serialize(self):
        return {"id": self.id}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/games')
def games():
    return jsonify([Game().serialize() for i in range(10)])
