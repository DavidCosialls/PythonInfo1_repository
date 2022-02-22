class C:
    def __init__ (self):

        self.company=''
        self.numberofaircrafts=0
        self.list=[0]
        self.pilots=0
        self.flightassistants=0
        self.ground=0

C1 = C()
C2= C ()
C1.company=raw_input('enter the name of the company: ')
C1.pilots=input('enter number of pilots: ')
C1.flightassistants=input('enter number of assistants: ')
C1.ground=input('enter number of ground workers: ')
C1.numberofaircrafts=input('enter number of aircrafts: ')
C1.list=[0]*C1.numberofaircrafts
i=0
while i<C1.numberofaircrafts:
    C1.list[i]=raw_input('Enter aircrafts callsign, aircraft type and year it was build')
    i+=1

C2.company=raw_input('enter the name of the company: ')
C2.pilots=input('enter number of pilots: ')
C2.flightassistants=input('enter number of assistants: ')
C2.ground=input('enter number of ground workers: ')
C2.numberofaircrafts=input('enter number of aircrafts: ')
C2.list=[0]*C2.numberofaircrafts
i=0
while i<C2.numberofaircrafts:
    C2.list[i]=raw_input('Enter aircrafts callsign, aircraft type and year it was build')
    i+=1

Cf= C ()
Cf.company=C1.company+C2.company
Cf.pilots=C1.pilots+C2.pilots
Cf.flightassistants=C1.flightassistants+C2.flightassistants
Cf.ground=C1.ground+C2.ground
Cf.numberofaircrafts=C1.numberofaircrafts+C2.numberofaircrafts
Cf.list=C1.list+C2.list

print Cf.__dict__
