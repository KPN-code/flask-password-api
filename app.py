from flask import Flask, jsonify, request
from flask_cors import CORS
from generator.password_generator import password_generator

app = Flask(__name__)
CORS(app)  # Sallii cross-origin pyynnöt

@app.route("/generate", methods=["GET"])
def generate():
    try:
        length = int(request.args.get("length", 12))
        symbols = request.args.get("symbols", "true").lower() == "true"
        pwd = password_generator(length=length, symbols=symbols)
        return jsonify({"password": pwd})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

