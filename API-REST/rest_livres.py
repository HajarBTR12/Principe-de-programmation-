from flask import Flask, jsonify, request

app = Flask(__name__)

# Liste des livres (données en mémoire)
livres = [
    {"id": 1, "titre": "Le Petit Prince",    "auteur": "Antoine de Saint-Exupéry", "annee": 1943},
    {"id": 2, "titre": "1984",               "auteur": "George Orwell",            "annee": 1949},
    {"id": 3, "titre": "L'Étranger",         "auteur": "Albert Camus",             "annee": 1942},
    {"id": 4, "titre": "Harry Potter T1",    "auteur": "J.K. Rowling",             "annee": 1997},
]

# Racine de l'API
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des livres !"

# GET : récupérer tous les livres
@app.route('/livres', methods=['GET'])
def get_livres():
    return jsonify(livres)

# POST : ajouter un livre
@app.route('/livres', methods=['POST'])
def add_livre():
    new_livre = request.get_json()       # Récupère les données du client
    new_livre['id'] = len(livres) + 1   # ID automatique
    livres.append(new_livre)
    return jsonify(new_livre), 201       # 201 = création réussie

# GET : récupérer un livre par son ID
@app.route('/livres/<int:id>', methods=['GET'])
def get_livre(id):
    livre = next((l for l in livres if l['id'] == id), None)
    if livre:
        return jsonify(livre)
    return jsonify({"erreur": "Le livre n'existe pas"}), 404

# PUT : modifier un livre
@app.route('/livres/<int:id>', methods=['PUT'])
def update_livre(id):
    livre = next((l for l in livres if l['id'] == id), None)
    if not livre:
        return jsonify({"erreur": "Le livre n'existe pas"}), 404
    data = request.get_json()
    livre.update(data)
    return jsonify(livre)

# DELETE : supprimer un livre
@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_livre(id):
    global livres
    livres = [l for l in livres if l['id'] != id]
    return jsonify({"message": "Livre supprimé"}), 200

# GET : nombre total de livres
@app.route('/livres/count', methods=['GET'])
def get_count():
    return jsonify({"nombre_de_livres": len(livres)})

# GET : livres publiés une année donnée
@app.route('/livres/count/<int:annee>', methods=['GET'])
def get_count_annee(annee):
    total = sum(1 for l in livres if l['annee'] == annee)
    return jsonify({"annee": annee, "total_livres": total})

if __name__ == '__main__':
    app.run(debug=True)
