from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
con=sqlite3.connect('database.db')

@app.route('/')
def fun1():
    return render_template('index.html')



app.run()