from typing import List
from utils import random_float
from random import randrange as random_int
from bounding_box import BoundingBox, Vector2
from datetime import datetime

class TrackerData():
    def __init__(self, bpm: int, lat: float, log: float, speed: float, time: datetime, distance: float):
        self.bpm = bpm
        self.lat = lat
        self.log = log
        self.speed = speed
        self.time = time
        self.distance = distance


class Tracker():
    def __init__(self, list: List[TrackerData] = []):
        self.data = list
        
    def addTrackerData(self, data: TrackerData):
        self.data.append(data)
        
        return data
        
    def generateNewTrackerData(self, bounding_box: BoundingBox):
        bpm = random_int(70, 100)
        lat = random_int(bounding_box.getMinLat(), bounding_box.getMaxLat())
        log = random_int(bounding_box.getMinLog(), bounding_box.getMaxLog())
        speed = random_float(0, 45)
        time = datetime.now()
        distance = 0
        
        if(len(self.data) > 0):
            distance = self.data[-1].distance + random_float(0,5)
        
        return self.addTrackerData(TrackerData(bpm, lat, log, speed, time, distance))
        