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


@app.route('/add_work')
def add_work():
    return render_template('addwork.html', dates=mongo.db.dates.find(), emploees=mongo.db.emploees.find())


@app.route('/insert_work', methods=['POST'])
def insert_work():
    works = mongo.db.works
    works.insert_one(request.form.to_dict())
    return redirect(url_for('get_works'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
