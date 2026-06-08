from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/add")
def add_employee():
    # your existing code
    return "Employee Added"

@app.route("/view")
def view_employees():

    conn = mysql.connector.connect(
        host="mysql-service",
        user="root",
        password="root123",
        database="employee_db"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    result = cursor.fetchall()

    conn.close()

    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
