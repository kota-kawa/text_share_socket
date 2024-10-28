from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "https://text-share.project-kk.com"}})

# Socket.IOのCORSをHTTPSオリジンで制限
#socketio = SocketIO(app, cors_allowed_origins="https://text-share.project-kk.com")

socketio = SocketIO(app)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('text_change')
def handle_text_change(data):
    emit('update_text', data, broadcast=True)


@app.route('/test')
def test():
    return render_template('test.html')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    send(f"Echo: {message}")

if __name__ == '__main__':
    socketio.run(app, debug=True) 
