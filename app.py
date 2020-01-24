from flask import Flask, request, render_template
from flask_session import Session
from geojson import Point
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/linodeStreetTrees"
mongo = PyMongo(app)

@app.route('/')
def index():
    street_trees_points_query = dumps(mongo.db.linodeStreetTrees.find({}, {'_id': False}))
    street_trees_points = json.loads(street_trees_points_o)
    return render_template('base.html', street_trees_points=street_trees_points)

if __name__ == '__main__':
    app.debug=True
    app.run()