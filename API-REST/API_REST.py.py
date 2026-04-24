from flask import Flask, jsonify, request

# Création de l'application Flask
app = Flask(__name__)

# Base de données temporaire (stockée en mémoire)
students = [
    {"id": 1, "name": "Youcef", "age": 21},
    {"id": 2, "name": "Samir", "age": 41},
    {"id": 3, "name": "Hajar", "age":24},

]

@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"

# GET : récupérer tous les étudiants
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


# GET : récupérer un étudiant par son ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    # Recherche de l'étudiant par son ID
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student)
    return jsonify({"erreur": "L'étudiant n'existe pas"}), 404

# POST : ajouter un nouvel étudiant
@app.route('/students', methods=['POST'])
def add_student():
    # Récupère les données envoyées par le client
    new_student = request.get_json()
    # Attribue un ID automatiquement
    new_student['id'] = len(students) + 1
    students.append(new_student)
    # Code 201 = création réussie
    return jsonify(new_student), 201

# PUT : modifier un étudiant existant
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return jsonify({"erreur": "L'étudiant n'existe pas"}), 404
    # Récupère les nouvelles données
    data = request.get_json()
    # Met à jour les informations
    student.update(data)
    return jsonify(student)

# DELETE : supprimer un étudiant
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return jsonify({"message": "Étudiant supprimé"}), 200

# Lancement du serveur
if __name__ == '__main__':
    # debug=True affiche les erreurs et recharge automatiquement le serveur
    app.run(debug=True)