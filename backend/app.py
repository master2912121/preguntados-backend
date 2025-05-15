from flask import Flask, request, jsonify  # type: ignore
import os

app = Flask(__name__)

# Ruta absoluta al archivo
CARPETA = os.path.join(os.path.dirname(__file__), "data")
RUTA_ARCHIVO = os.path.join(CARPETA, "respuestas.txt")

# Asegurar que la carpeta existe
os.makedirs(CARPETA, exist_ok=True)

@app.route("/respuesta", methods=["POST"])
def guardar_respuesta():
    print("POST /respuesta recibido")  # Confirmar llegada de la petición
    data = request.json
    print("Datos recibidos:", data)

    if not data or 'pregunta' not in data or 'respuesta' not in data:
        print("Faltan datos en la petición")
        return jsonify({"error": "Faltan datos"}), 400

    try:
        with open(RUTA_ARCHIVO, "a", encoding="utf-8") as f:
            linea = f"{data['pregunta']}: {data['respuesta']}\n"
            print("Escribiendo:", linea.strip())
            f.write(linea)
        return jsonify({"mensaje": "Respuesta guardada"}), 200
    except Exception as e:
        print("Error al escribir el archivo:", e)
        return jsonify({"error": f"No se pudo guardar la respuesta: {str(e)}"}), 500


@app.route("/")
def home():
    return jsonify({"estado": "Servidor Flask funcionando correctamente"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
