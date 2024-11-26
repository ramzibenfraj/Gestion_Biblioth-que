from flask import Blueprint, request, jsonify
from config import mongo
from models.emprunt import create_emprunt, emprunt_to_dict
from bson import ObjectId

emprunt_bp = Blueprint('emprunt', __name__)

@emprunt_bp.route('/add', methods=['POST'])
def ajouter_emprunt():
    data = request.json
    emprunt = create_emprunt(data)
    mongo.db.emprunts.insert_one(emprunt)
    return jsonify({"message": "Emprunt enregistré"}), 201

@emprunt_bp.route('/emprunts', methods=['GET'])
def liste_emprunts():
    emprunts = mongo.db.emprunts.find()
    return jsonify([emprunt_to_dict(e) for e in emprunts]), 200

@emprunt_bp.route('/emprunts/<id>', methods=['GET'])
def obtenir_emprunt(id):
    emprunt = mongo.db.emprunts.find_one({"_id": ObjectId(id)})
    if not emprunt:
        return jsonify({"error": "Emprunt introuvable"}), 404
    return jsonify(emprunt_to_dict(emprunt)), 200

@emprunt_bp.route('/update/<id>', methods=['PUT'])
def modifier_emprunt(id):
    data = request.json
    mongo.db.emprunts.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Emprunt mis à jour"}), 200

@emprunt_bp.route('/delete/<id>', methods=['DELETE'])
def supprimer_emprunt(id):
    mongo.db.emprunts.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Emprunt supprimé"}), 200

@emprunt_bp.route("/statsEmp", methods=["GET"])
def get_stats():
    emprunts_count = mongo.db.emprunts.count_documents({})
    return jsonify({
        "empruntsCount": emprunts_count
    })