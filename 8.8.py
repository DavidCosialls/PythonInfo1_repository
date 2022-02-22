#8.8

class TflightPlan:
    def __init__ (pas):
        pas.departureairportcode=0
        pas.arrivalairportcode=0
        pas.flightlevel=0.0
        pas.departuretime=0.0
class TwayPoint:
    def __init__ (pos):
        pos.x=0
        pos.y=0
        pos.z=0
        pos.estimatedtimeover=0

F= TflightPlan ()
F.departuretime=14.30
print ("Departute time,", F.departuretime)
t=input ("Enter time after departure")
J= TwayPoint ()
flightduration=5
J.estimatedtimeover=flightduration-t
J.x=194578
J.y=5478
J.z=5200
F.departureairportcode=878465
F.arrivalairportcode=874576
F.flightlevel=J.z

print J.__dict__




