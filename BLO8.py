class Tgym:
    def __init__ (sto):
        sto.gym_name=""
        sto.people=[[""]]
        sto.machines=[['']]

class Tperson:
    def __init__ (per):
        per.name=""
        per.numbertraineddays=0
        per.burnedKcal=0

class Tmachine:
    def __init__ (mac):
        mac.description=""
        mac.identificator_number=0

gym= Tgym ()
person1= Tperson()
machine1= Tmachine ()

person1.name=raw_input('Person1 name:')
person1.numbertraineddays=input("Number of trained days")
person1.burnedKcal=input("Kcal burned")

machine1.description=input('enter machine description')
machine1.identificator_number=input('Enter machine identificator number')

gym.name=raw_input('enter gym_s name')
gym.people[0]=person1.name
gym.machines[0]=machine1.name



