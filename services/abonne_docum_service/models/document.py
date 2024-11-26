from flask_pymongo import ObjectId

def document_to_dict(document):
    return {
        "id": str(document["_id"]),
        "titre": document["titre"],
        "auteur": document["auteur"],
        "genre": document["genre"],
        "disponibilite": document["disponibilite"]
    }

def create_document(data):
    return {
        "titre": data.get("titre"),
        "auteur": data.get("auteur"),
        "genre": data.get("genre"),
        "disponibilite": data.get("disponibilite", True)
    }
