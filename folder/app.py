from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)

def baza():
    connection = sqlite3.connect("dataschools.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grade_table (ID INTEGER PRIMARY KEY AUTOINCREMENT, score REAL)
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students_table(ID INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, id_grade INTEGER)
    """)
    connection.commit()
    connection.close()

baza()


@app.route("/", methods=["GET", "POST"])
def home():
    gr = ""
    name = "Admin"

    connection = sqlite3.connect("dataschools.db")
    cursor = connection.cursor()

    try:
        if request.method == "POST":

            if "name" in request.form and "grade" in request.form:
                imie = request.form.get("name")
                ocena = float(request.form.get("grade"))

                cursor.execute(
                    "INSERT INTO grade_table (score) VALUES (?)",
                    (ocena,)
                )
                grade_id = cursor.lastrowid

                cursor.execute(
                    "INSERT INTO students_table (fname, id_grade) VALUES (?, ?)",
                    (imie, grade_id)
                )

            if "sname" in request.form:
                cursor.execute("""
                    SELECT g.score 
                    FROM students_table s 
                    JOIN grade_table g ON s.id_grade = g.id 
                    WHERE s.fname = ?
                """, (request.form.get("sname"),))

                wynik = cursor.fetchone()
                gr = wynik[0] if wynik else "brak"

        cursor.execute("SELECT score FROM grade_table")
        wszystkie_oceny = [w[0] for w in cursor.fetchall() if w[0] is not None]

        countstu = len(wszystkie_oceny)

        if countstu > 0:
            srednia = sum(wszystkie_oceny) / countstu
            excellent = sum(1 for g in wszystkie_oceny if g >= 90)
            fail = sum(1 for g in wszystkie_oceny if g < 50)
            highest = max(wszystkie_oceny)
            lowest = min(wszystkie_oceny)
        else:
            srednia = excellent = fail = highest = lowest = 0

    except Exception as e:
        connection.close()
        return f"Błąd: {e}"

    connection.close()

    return render_template(
        "index.html",
        name=name,
        grade=gr,
        countstu=countstu,
        excellent=excellent,
        fail=fail,
        highest=highest,
        lowest=lowest,
        srednia=round(srednia, 2),
        css=url_for("static", filename="style.css")
    )
    
if __name__ == "__main__":
    app.run(debug=True)
    
        
#        cursor.execute("""
#            INSERT INTO Student_table(firstname, lastname, age)
#            VALUES (?, ?, ?)
#            """, (
#            request.form["firstname"],
#            request.form["lastname"],
#            request.form["age"]
#        ))
#    quantity = len(students)
#    sum_test = 0
#    for student in students:
#        sum_test += int(student["test"])
#    if quantity > 0:
#       average = sum(int(student["test"]) for student in students) / quantity
#   else:
#        average = 0




#connection.commit()

#cursor.execute("SELECT * FROM Student_table")

#print(cursor.fetchall())

#connection.close()