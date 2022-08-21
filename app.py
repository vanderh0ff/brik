from flask import Flask, render_template
from data.db import db

app = Flask(__name__)

@app.route("/")
def hello_world():
        return render_template('index.html', comments=db.list_collection_names())
