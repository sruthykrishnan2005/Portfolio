from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
con=sqlite3.connect('database.db')

@app.route('/')
def home():
    return render_template('home.html')

    
@app.route('/about')
def about():
    return render_template('about.html')

app.run()