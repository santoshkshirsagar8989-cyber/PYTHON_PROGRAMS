# Flask is a micro web frame work writeen in python
# Flask concept 
#   Browser(crome)request-->Flask-->python code
#   Browser(crome)<--response<--Flask<--python code
from flask import Flask
app = Flask(__name__)
Menus=[
    {"item":"Pizza","price":100},
    {"item":"Burger","price":50},
    {"item":"Sandwich","price":75},
    {"item":"Pasta","price":120}
]
@app.route('/') # this handle URL
def home():
    HTML="<h1>Welcome to our Canteen</h1>"
    HTML +="<ul>"
    for item in Menus:
        HTML += f"<li>{item['item']}: {item['price']} rs</li>"
    HTML += "</ul>"
    return HTML
@app.route('/Contact')
def contact():
    return "<h1>Contact Us</h1><p>Phone: 123-456-7890</p><p>Email: info@canteen.com</p>"
if __name__ == '__main__':
    app.run(debug=True)