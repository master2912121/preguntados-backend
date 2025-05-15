from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "interacciones_render.txt"

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    username = data.get('username')
    card = data.get('card')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[INFO] {timestamp}: {username} seleccionó {card}"
    print(log)

    with open(DATA_FILE, "a") as file:
        file.write(f"{timestamp} - {username} seleccionó {card}\n")
    return jsonify({"status": "ok"})

@app.route('/')
def index():
    with open('./frontend/index.html', 'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
