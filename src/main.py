from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from bounding_box import *
from tracker import Tracker

app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'
bounding_box = BoundingBox()
tracker = Tracker()

@cross_origin()
@app.route("/")
def basic_route():
    return "API working"

@cross_origin()
@app.route("/set-bound", methods = ["POST"])
def set_boundaries():
    body = request.json
    bounding_box.first_point = listToVector2(body["first"])
    bounding_box.second_point = listToVector2(body["second"])
    bounding_box.third_point = listToVector2(body["third"])
    bounding_box.fourth_point = listToVector2(body["fourth"])
    return "Bounding Box defined"

@cross_origin()
@app.route("/reset-tracker", methods = ["POST"])
def reset_tracker():
    tracker.data = []
    return "Tracker reseted"

@cross_origin()
@app.route("/new-data", methods = ["GET"])
def new_tracker():
    if(not bounding_box.isOk()):
        return "Define a bounding box first"
    data = tracker.generateNewTrackerData(bounding_box)
    print(data.bpm)
    return {
        "bpm" : data.bpm,
        "lat": data.lat,
        "log": data.log,
        "speed": data.speed,
        "time": data.time,
        "distance": data.distance
    }


app.run(host="0.0.0.0", port=3000)
