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
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS userinfo
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 password TEXT NOT NULL
                 )
                 ''')

    column_names = [row[1] for row in conn.execute("PRAGMA table_info(userinfo)").fetchall()]
    if 'role' not in column_names:
        conn.execute("ALTER TABLE userinfo ADD COLUMN role TEXT DEFAULT 'customer'")
    
    conn.commit()
    conn.close()

init_db()

if __name__ == "__main__":
    app.run(debug=True)