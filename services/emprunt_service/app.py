from flask import Flask
from flask_cors import CORS
from routes.emprunt_routes import emprunt_bp

app = Flask(__name__)

# Enable CORS for all origins
CORS(app, resources={r"/*": {"origins": "*"}})

# Register blueprints
app.register_blueprint(emprunt_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3003, debug=True)
