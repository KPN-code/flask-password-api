from flask import Flask, jsonify, request
from generator.password_generator import password_generator

app = Flask(__name__)

@app.route("/generate", methods=["GET"])
def generate():
    length = int(request.args.get("length", 12))
    symbols = request.args.get("symbols", "true").lower() == "true"
    pwd = password_generator(length=length, symbols=symbols)
    return jsonify({"password": pwd})

if __name__ == "__main__":
    app.run(debug=True)
