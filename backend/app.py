from flask import Flask, jsonify
from backend.models import Dossier

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Backend API en ligne"

@app.route("/dossier/<int:id>")
def get_dossier(id):
    dossier = Dossier.get_by_id(id)
    if dossier:
        return jsonify(success=True, data=dossier.to_dict())
    else:
        return jsonify(success=False, message="Patient non trouvé")

if __name__ == "__main__":
    app.run(debug=True)