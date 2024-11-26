from flask import Blueprint, request, jsonify
from config import mongo
from models.abonne import create_abonne, abonne_to_dict
from bson import ObjectId

abonne_bp = Blueprint('abonne', __name__)

@abonne_bp.route('/addabonne', methods=['POST'])
def ajouter_abonne():
    data = request.json
    abonne = create_abonne(data)
    mongo.db.abonnes.insert_one(abonne)
    return jsonify({"message": "Abonné ajouté avec succès"}), 201

@abonne_bp.route('/abonnes', methods=['GET'])
def liste_abonnes():
    abonnes = mongo.db.abonnes.find()
    return jsonify([abonne_to_dict(a) for a in abonnes]), 200

@abonne_bp.route('/abonnes/<id>', methods=['GET'])
def obtenir_abonne(id):
    abonne = mongo.db.abonnes.find_one({"_id": ObjectId(id)})
    if not abonne:
        return jsonify({"error": "Abonné introuvable"}), 404
    return jsonify(abonne_to_dict(abonne)), 200

@abonne_bp.route('/updateabonne/<id>', methods=['PUT'])
def modifier_abonne(id):
    data = request.json
    mongo.db.abonnes.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Abonné mis à jour"}), 200

@abonne_bp.route('/deleteabonne/<id>', methods=['DELETE'])
def supprimer_abonne(id):
    mongo.db.abonnes.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Abonné supprimé"}), 200

@abonne_bp.route("/stats", methods=["GET"])
def get_stats():
    abonnés_count = mongo.db.abonnes.count_documents({})
    return jsonify({
        "abonnésCount": abonnés_count
    })
