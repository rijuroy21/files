from flask import Flask,render_template,redirect,request,send_from_directory
import sqlite3
app = Flask(__name__)
con=sqlite3.connect('database.db')

@app.route('/')
def fun1():
    return render_template('index.html')

@app.route("/view_resume")
def view_resume():
    return send_from_directory(directory="static/images", path="Riju Roy cv.pdf")


@app.route('/submit', methods=['POST'])
def submit_form():
  
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contact (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        subject TEXT,
                        message TEXT NOT NULL)''')
    cursor.execute("INSERT INTO contact (name, email, subject, message) VALUES (?, ?, ?, ?)",
                   (name, email, subject, message))
    conn.commit()
    conn.close()

    return redirect('/')

app.run()