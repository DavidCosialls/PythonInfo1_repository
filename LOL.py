'''
Point definition:
A point has a latitude, a longitude, an elevation.
In addition, it has a flag which indicates if the point is interesting
and the name of the picture of the location pointed.
'''
class Point:
 def __init__ (self):
     self.latitude = 0.0
     self.longitude = 0.0
     self.elevation = 0.0
     self.isInteresting = False
     self.imageFile = ""
'''
Route definition
A route has a name, a description and a list of points.
'''
class Route:
 def __init__ (self):
     self.name = ""
     self.description = ""
     self.trackPoints = [] # each element of type Point
rw = Route()
rw.name = "my route"
rw.description = "it is a beatiful one"
p = Point()
p.latitude = 2.23
p.longitude = 1.25
p.elevation = 567.44
rw.trackPoints.append(p)
print rw.__dict__
