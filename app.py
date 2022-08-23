from flask import Flask, render_template
from data.db import db

app = Flask(__name__)

@app.route("/")
def hello_world():
        return render_template('index.html', comments=db.list_collection_names())

@app.route("/classes")
def show_classes():
        classes = db.tasks.distinct('subject')
        return render_template("classes.html",classes=classes)

@app.route("/classes/<class_name>")
def show_class(class_name):
        query = {
                "subject": class_name
        }
        this_class_tasks = db.tasks.find(query)
        return render_template('show_class.html', class_name=class_name, tasks=this_class_tasks)
