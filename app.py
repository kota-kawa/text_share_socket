from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('text_change')
def handle_text_change(data):
    emit('update_text', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
