from flask import Flask, request, jsonify # type: ignore
import os

app = Flask(__name__)

@app.route("/respuesta", methods=["POST"])
def guardar_respuesta():
    data = request.json
    if not data or 'pregunta' not in data or 'respuesta' not in data:
        return jsonify({"error": "Faltan datos"}), 400

    with open("respuestas.txt", "a") as f:
        f.write(f"{data['pregunta']}: {data['respuesta']}\n")

    return jsonify({"mensaje": "Respuesta guardada"}), 200

@app.route("/")
def home():
    return jsonify({"estado": "Servidor Flask funcionando correctamente"})


app.run(host="0.0.0.0", port=80)
