import os
import sqlite3
from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "santosh"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "myproject.db")

# 2 functions
def get_db():
    """"Database Connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create Table"""
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS menus
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 price INTEGER NOT NULL)
                 ''')
    

    conn.execute('''CREATE TABLE IF NOT EXISTS beverages(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL UNIQUE)
                 ''')
    default_beverages = ['Tea', 'Coffee', 'Water']
    for beverage in default_beverages:
        try:
            conn.execute('INSERT INTO beverages (name) values (?)', (beverage,))
        except sqlite3.IntegrityError:
            # Ignore if the beverage already exists
            pass
    
    conn.commit()
    conn.close()

init_db()

if __name__ == "__main__":
    app.run(debug=True)