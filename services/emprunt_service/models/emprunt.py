from flask_pymongo import ObjectId

def emprunt_to_dict(emprunt):
    return {
        "id": str(emprunt["_id"]),
        "abonne_id": str(emprunt["abonne_id"]),
        "document_id": str(emprunt["document_id"]),
        "date_emprunt": emprunt["date_emprunt"],
        "date_retour": emprunt.get("date_retour")
    }

def create_emprunt(data):
    return {
        "abonne_id": ObjectId(data.get("abonne_id")),
        "document_id": ObjectId(data.get("document_id")),
        "date_emprunt": data.get("date_emprunt"),
        "date_retour": data.get("date_retour")
    }
