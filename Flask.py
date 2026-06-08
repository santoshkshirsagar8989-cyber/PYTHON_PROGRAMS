# Flask is a micro web frame work writeen in python
# Flask concept 
#   Browser(crome)request-->Flask-->python code
#   Browser(crome)<--response<--Flask<--python code
from flask import Flask
app = Flask(__name__)
@app.route('/') # this handle URL
def home():
    return "<h1>Welcome to Flask</h1>"
if __name__ == '__main__':
    app.run(debug=True)