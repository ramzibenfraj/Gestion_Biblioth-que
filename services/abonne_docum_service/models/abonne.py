from flask_pymongo import ObjectId

def abonne_to_dict(abonne):
    return {
        "id": str(abonne["_id"]),
        "nom": abonne["nom"],
        "email": abonne["email"],
        "telephone": abonne["telephone"]
    }

def create_abonne(data):
    return {
        "nom": data.get("nom"),
        "email": data.get("email"),
        "telephone": data.get("telephone")
    }

