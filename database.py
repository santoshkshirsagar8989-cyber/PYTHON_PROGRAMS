import sqlite3
from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "santosh"

# 2 functions
def get_db():
    """"Database Connection"""
    conn = sqlite3.connect('myproject.db')
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
    
if __name__ == "__main__":
    init_db()
    app.run(debug=True)