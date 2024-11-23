class Vector2:    
    def __init__(self, lat: float, log: float):
        self.lat = lat
        self.log = log
        


class BoundingBox:
    def __init__(self, first_point: Vector2 = Vector2(None,None), second_point: Vector2=Vector2(None,None), third_point:Vector2=Vector2(None,None), fourth_point:Vector2 = Vector2(None,None)):
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point
        self.fourth_point = fourth_point
        
    def isOk(self):
        list = [self.first_point, self.second_point, self.third_point, self.fourth_point]
        for item in list:
            if(item.lat == None or item.log == None):
                return False
        return True
    
    def getMinLat(self):
        return min([self.first_point.lat, self.second_point.lat, self.third_point.lat, self.fourth_point.lat])
    
    def getMaxLat(self):
        return max([self.first_point.lat, self.second_point.lat, self.third_point.lat, self.fourth_point.lat])
    
    def getMaxLog(self):
        return max([self.first_point.log, self.second_point.log, self.third_point.log, self.fourth_point.log])

    def getMinLog(self):
        return min([self.first_point.log, self.second_point.log, self.third_point.log, self.fourth_point.log])
    
    
def listToVector2(list: list):
    return Vector2(list[0], list[1])
