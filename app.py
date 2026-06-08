from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():

    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root123",
        database="employee_db"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT NOW()")

    result = cursor.fetchone()

    conn.close()

    return f"MySQL Connected: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
