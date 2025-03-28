from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})

# テキストを保存する変数
shared_text = ""

@app.route('/')
def index():
    return render_template('text_share.html')

@app.route('/text_change', methods=['POST'])
def handle_text_change():
    global shared_text
    data = request.json
    shared_text = data.get('text', '')
    return jsonify({'status': 'Text updated', 'text': shared_text})

@app.route('/get_text', methods=['GET'])
def get_text():
    return jsonify({'text': shared_text})

if __name__ == '__main__':
    app.run(debug=True)
