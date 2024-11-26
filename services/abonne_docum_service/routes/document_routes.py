from flask import Blueprint, request, jsonify
from config import mongo
from models.document import create_document, document_to_dict
from bson import ObjectId

document_bp = Blueprint('document', __name__)

@document_bp.route('/adddocument', methods=['POST'])
def ajouter_document():
    data = request.json
    document = create_document(data)
    mongo.db.documents.insert_one(document)
    return jsonify({"message": "Document ajouté"}), 201

@document_bp.route('/documents', methods=['GET'])
def liste_documents():
    documents = mongo.db.documents.find()
    return jsonify([document_to_dict(d) for d in documents]), 200

@document_bp.route('/documents/<id>', methods=['GET'])
def obtenir_document(id):
    document = mongo.db.documents.find_one({"_id": ObjectId(id)})
    if not document:
        return jsonify({"error": "Document introuvable"}), 404
    return jsonify(document_to_dict(document)), 200

@document_bp.route('/updatedocument/<id>', methods=['PUT'])
def modifier_document(id):
    data = request.json
    mongo.db.documents.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Document mis à jour"}), 200

@document_bp.route('/deletedocument/<id>', methods=['DELETE'])
def supprimer_document(id):
    mongo.db.documents.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Document supprimé"}), 200

@document_bp.route("/statsDoc", methods=["GET"])
def get_stats():
    documents_count = mongo.db.documents.count_documents({})
    return jsonify({
        "documentsCount": documents_count
    })