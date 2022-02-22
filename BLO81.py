class Tperson:
    def _init_ (self):
        self.name=''
        self.days=0
        self.burnedKcal=0
class Tmachine:
    def _init_ (self):
        self.description=''
        self.identification=0
class Tgym:
    def _init_ (self):
        self.namegym=''
        self.trackTperson=[]
        self.trackTmachine=[]
        self.people=0
        self.machines=0

a = Tperson()
b = Tmachine()
c = Tgym()

c.namegym=raw_input('enter the name of the gym: ')
c.machines=input('enter number of machines: ')
c.people=input('enter number of people: ')
i=0
while i<c.people:
    a.name=raw_input('enter a name: ')
    a.days=input('enter number of days that has trained: ')
    a.burnedKcal=input('enter amount of burned Kcal: ')
    c.trackTperson.append(a)
    i=i+1
j=0
while j<c.machines:
    b.description=raw_input('enter description of machine: ')
    b.identification=input('enter identification number: ')
    c.trackTmachine.append(b)
    j=j+1
print c. _dict_
