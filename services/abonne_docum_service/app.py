from flask import Flask
from flask_cors import CORS
from routes.abonne_routes import abonne_bp
from routes.document_routes import document_bp

app = Flask(__name__)

# Enable CORS for all origins
CORS(app, resources={r"/*": {"origins": "*"}})

# Register blueprints
app.register_blueprint(abonne_bp, url_prefix="/")
app.register_blueprint(document_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)
