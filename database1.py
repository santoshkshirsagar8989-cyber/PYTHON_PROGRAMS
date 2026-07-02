import sqlite3
from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "kshirsagar"

# 2 functions
def get_db():
    """"Database Connection"""
    conn = sqlite3.connect('myorder.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create Table"""
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS allorder
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 quantity INTEGER NOT NULL,
                 price INTEGER NOT NULL)
                 ''')
    
    conn.commit()
    conn.close()

init_db()

if __name__ == "__main__":

    app.run(debug=True)