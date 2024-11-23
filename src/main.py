from flask import Flask
from bounding_box import *
from flask import request
from tracker import Tracker

app = Flask(__name__)
bounding_box = BoundingBox()
tracker = Tracker()

@app.route("/set-bound", methods = ["POST"])
def set_boundaries():
    body = request.json
    bounding_box.first_point = listToVector2(body["first"])
    bounding_box.second_point = listToVector2(body["second"])
    bounding_box.third_point = listToVector2(body["third"])
    bounding_box.fourth_point = listToVector2(body["fourth"])
    return "Bounding Box defined"


@app.route("/reset-tracker", methods = ["POST"])
def reset_tracker():
    tracker.data = []
    return "Tracker reseted"
    
@app.route("/new-tracker", methods = ["GET"])
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