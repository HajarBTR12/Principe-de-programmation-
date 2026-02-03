from flask import Flask, jsonify,request

# Créer l'application Flask
app = Flask(__name__)

# Définir les données
students = [
    {"id": 1, "name": "youcef", "age": 21},
    {"id": 2, "name": "samir", "age": 41}
]

@app.route('/')
def home():
    
    return "Bienvenue dans l'API de gestion des étudants!"
@app.route('/students', methods=['GET'])
def get_students():
    "jsonify trasforme la liste students en json"
    return jsonify(students)

#ajt in éeudiant (post)
@app.route('/students', methods=['POST'])
def add_student():
    new_student=request.get_json()
    #pr recuperer les donne envoye pas le client
    new_student['id']=len(students)+1
    #attribuer un numéro de manière icrémentable
    students.append(new_student)
    return jsonify(new_student),201
#le code 201 pour dire cetion réssie


#afficher un etudiant sachant sn identifiant
@app.route('/students/<int:id>',methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id']==id), None)
    if student :
        return jsonify(student)
    return jsonify({"erreur":"l'etudiant n'existe  pas !"}),404
#Mettre un jour un étudiant PUT
@app.route('/students/<int:id>',methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id']==id), None)
    if not student :
        return jsonify({"message":"Etudiant non trouvé!"}),404
    data=request.get_json()
    student.update(data)#mise a jour des données
    return jsonify(student)
#Supprimer un etudiant DELETE
@app.route('/students/<int:id>',methods=['DELETE'])
def delete_student(id):
    global students
    student = [s for s in students if s['id']!=id]
    return jsonify({"message":"Etudiant supprimé"}),200
   

if __name__ == "__main__":
    app.run(debug=True)