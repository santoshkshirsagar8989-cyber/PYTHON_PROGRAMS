import sqlite3
from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "santosh"

# 2 functions
def get_db():
    """"Database Connection"""
    conn = sqlite3.connect('userinfo.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create Table"""
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS userinfo
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 password NUMBER NOT NULL
                 )
                 ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)