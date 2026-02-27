from db import get_conection

def get_all_students():
    conn = get_conection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return result
def get_student_by_id(student_id):
    conn = get_conection()
    cursor = conn.cursor(dictionary = True)
    
    query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(query,(student_id,))
    
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return student
def add_student(student_data):
    conn = get_conection()
    cursor = conn.cursor(dictionary=True)
    query = "INSERT INTO students (student_id, name, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (student_data["student_id"], student_data["name"], student_data["age"]))
    conn.commit()  
    cursor.close()
    conn.close()
    return {"message": "Student added successfully"}


def delete_student(student_id):
    conn = get_conection()
    cursor = conn.cursor()
    # Vérifier si l'étudiant existe
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    student = cursor.fetchone()
    if student is None:
        return {"error": "Student not found"}, 404
    
    query = "DELETE FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()  # Commit de la transaction
    cursor.close()
    conn.close()
    return {"message": "Student deleted successfully"}