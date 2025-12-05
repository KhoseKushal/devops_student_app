from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

db_host = os.environ.get("DB_HOST", "localhost")
db_user = os.environ.get("DB_USER", "root")
db_password = os.environ.get("DB_PASSWORD", "")
db_name = os.environ.get("DB_NAME", "studentdb")

def get_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

@app.route("/", methods=["GET", "POST"])
def form():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        city = request.form.get("city")
        phone = request.form.get("phone")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), city VARCHAR(255), phone VARCHAR(50))")
        cursor.execute("INSERT INTO students (name, email, city, phone) VALUES (%s, %s, %s, %s)", (name, email, city, phone))
        conn.commit()
        cursor.close()
        conn.close()

        message = "Data Saved Successfully!"
    return render_template("form.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
