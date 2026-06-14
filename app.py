# Flask is a micro web frame work writeen in python
# Flask concept 
#   Browser(crome)request-->Flask-->python code
#   Browser(crome)<--response<--Flask<--python code
from tkinter import Menu

from flask import Flask, render_template

app = Flask(__name__)

Menus = [
    {"name":"pizza","price":100},
    {"name":"Burger","price":50},
    {"name":"Sandwich","price":75},
    {"name":"Pasta","price":120}
]


@app.route('/')
def home():
    return render_template('home.html',Menus=Menus)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)