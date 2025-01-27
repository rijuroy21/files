from flask import Flask,render_template
import sqlite3

app= Flask(__name__)

@app.route('/')
def index():
    Database='/home/novavi/Desktop/Riju/Flask/sample_project/mydb.db'
    con=sqlite3.connect(Database)
    cursor=con.cursor()
    print(cursor)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)