from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    "host": "mysql-service",
    "user": "root",
    "password": "root123",
    "database": "employee_db"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/")
def home():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        employees=employees
    )


@app.route("/add", methods=["POST"])
def add_employee():

    name = request.form["name"]
    role = request.form["role"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees(name, role) VALUES(%s,%s)",
        (name, role)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete_employee(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=%s",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
