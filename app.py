from flask import Flask, render_template, request, redirect, url_for
import sqlite3


def get_db():
    conn = sqlite3.connect("assignments.db")
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)

@app.route("/")
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks "
    "(id INTEGER PRIMARY KEY, subject TEXT, description TEXT, due_date TEXT, done INTEGER DEFAULT 0)")
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_tasks():
    subject = request.form['subject']
    description = request.form['description']
    due_date = request.form['due_date']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (subject, description, due_date, done) VALUES (?, ?, ?, ?)",
                   (subject, description, due_date, 0))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/complete", methods=["POST"])
def complete_task():
        conn = get_db()
        cursor = conn.cursor()
        task_id = request.form['id']
        cursor.execute("UPDATE tasks SET done = ? WHERE id =?",
                   ( 1, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

@app.route("/delete", methods= ['POST'])
def delete_task():
    conn = get_db()
    cursor = conn.cursor()
    task_id = request.form['id']
    cursor.execute("DELETE FROM tasks WHERE id =?",
                   (task_id, ))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)