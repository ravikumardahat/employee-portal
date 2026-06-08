from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/add")
def add_employee():

    conn = mysql.connector.connect(
        host="mysql-service",
        user="root",
        password="root123",
        database="employee_db"
    )

    cursor = conn.cursor()

    sql = """
    INSERT INTO employees(name, role)
    VALUES(%s,%s)
    """

    values = ("Ravi", "DevOps")

    cursor.execute(sql, values)

    conn.commit()

    conn.close()

    return "Employee Added"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
