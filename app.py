# Tuodaan tarvittavat kirjastot
from flask import Flask, jsonify, request          # Flask: kevyt web-palvelin, jsonify: muuntaa Python-olion JSON-muotoon, request: käsittelee sisään tulevat pyynnöt
from flask_cors import CORS                        # CORS: sallii pyyntöjen tulevan muista verkkotunnuksista (Cross-Origin Resource Sharing)
from generator.password_generator import password_generator  # Tuodaan salasanojen generointifunktio omasta tiedostosta

# Luodaan Flask-sovellus
app = Flask(__name__)

# Sallitaan CORS, eli pyyntöjä voidaan tehdä myös eri domainilta (esim. frontti localhostista)
CORS(app)

# Määritellään reitti /generate, sallii vain GET-metodin
@app.route("/generate", methods=["GET"])
def generate():
    try:
        # "length" -> muunnetaan se kokonaisluvuksi. (oletus 12)
        length = int(request.args.get("length", 12))
        
        # "symbols" kertoo käytetäänkö erikoismerkkejä. Oletus on "true".
        # Muutetaan arvo pieniksi kirjaimiksi -> onko se "true".
        symbols = request.args.get("symbols", "true").lower() == "true"
        pwd = password_generator(length=length, symbols=symbols)
        
        # Palautetaan generoitu salasana (json)
        return jsonify({"password": pwd})
    
    except Exception as e:
        # virheviesti JSON-muodossa
        return jsonify({"error": str(e)}), 400  # 400 tarkoittaa "Bad Request" 
