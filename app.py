# Flask is a micro web frame work writeen in python
# Flask concept 
#   Browser(crome)request-->Flask-->python code
#   Browser(crome)<--response<--Flask<--python code
from flask import Flask, render_template

app = Flask(__name__)

Menus = [
    {"item":"Pizza","price":100},
    {"item":"Burger","price":50},
    {"item":"Sandwich","price":75},
    {"item":"Pasta","price":120}
]

@app.route('/')
def home():
    return render_template('home.html', Menu=Menus)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)