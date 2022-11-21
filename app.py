from flask import Flask
from flask import render_template


## Start Flask application
app = Flask(__name__)

## Create Web App Routes

@app.route("/")
def index():
    return render_template("index.html")