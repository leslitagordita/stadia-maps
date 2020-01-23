import re
from flask import Flask, redirect, request, render_template, session, send_from_directory
from flask_session import Session
from geojson import Point
from flask_pymongo import PyMongo
from bson.json_util import dumps

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/linodeStreetTrees2"
mongo = PyMongo(app)

@app.route('/')
def main():
    street_trees_points = dumps(mongo.db.linodeStreetTrees2.find({}, {'_id': False}))
    return render_template('base_2.html', street_trees_points=street_trees_points)

if __name__ == '__main__':
    app.debug=True
    app.run()