from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongo", 27017)
db = client.notasdb
notas = db.notas

@app.route('/')
def index():
    return "API de Notas funcionando!"

@app.route('/notas', methods=['POST'])
def crear_nota():
    data = request.get_json()
    nueva = {"titulo": data["titulo"], "contenido": data["contenido"]}
    notas.insert_one(nueva)
    return jsonify({"mensaje": "Nota creada"}), 201

@app.route('/notas', methods=['GET'])
def obtener_notas():
    todas = list(notas.find({}, {'_id': 0}))
    return jsonify(todas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)