import os
import sqlite3
from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "santosh"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "userinfo.db")

# 2 functions
def get_db():
    """"Database Connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS userinfo
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 password TEXT NOT NULL
                 )
                 ''')

    try:
        conn.execute("ALTER TABLE userinfo ADD COLUMN role TEXT DEFAULT 'customer'")
    except Exception:
        pass

    
    conn.commit()
    conn.close()

init_db()

if __name__ == "__main__":
    app.run(debug=True)