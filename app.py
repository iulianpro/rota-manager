from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for
import os
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'rota_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_works')
def get_works():
    return render_template("works.html", works=mongo.db.works.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
