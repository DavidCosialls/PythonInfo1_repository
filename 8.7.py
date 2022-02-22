#8.7

class Agenda:
    def __init__ (day):
        day.date=[0]
        day.duration=0.0
        day.place=""
        day.description=""

class Tdate:
    def __init__ (int):
        int.year=[0]
        int.month=[0]
        int.day=[0]

r=input ("number or repetitions")
w=raw_input ("How often (every day or every week)")
i=1
j=0
a= Agenda ()
T= Tdate ()
a.date=list(raw_input("Enter de date DD/MM/YYYY"))
dd=float(a.date[0]+a.date[1])
mm=float(a.date[3]+a.date[4])
yy=float(a.date[6]+a.date[7]+a.date[8]+a.date[9])
M=[[dd,"/",mm,"/",yy]]*r
MW=[[dd,"/",mm,"/",yy]]*(r)*7
if w=="every week":
    T.year=[0]*(r-1)*7
    T.month=[0]*(r-1)*7
    T.day=[0]*(r-1)*7
elif w=="every day":
    T.year=[0]*(r-1)
    T.month=[0]*(r-1)
    T.day=[0]*(r-1)
#suposed all months have 31 days
while i<r:
    if w=="every day":
        if dd<31:

            dd+=1
        elif dd==31:
            dd=1
            if mm<12:
                mm+=1
            elif mm==12:
                mm=1
                yy+=1
            M[i]=[dd,"/",mm,"/",yy]
        T.year[i-1]=yy
        T.month[i-1]=mm
        T.day[i-1]=dd

    if w=="every week":
        n=0

        T.year[j]=yy
        T.month[j]=mm
        T.day[j]=dd
        if dd<31:
            dd+=7
        elif dd>31:
            dd=31-dd
            if mm<12:
                mm+=1
            elif mm==12:
                mm=1
                yy+=1
        elif dd==31:
            dd=1
            if mm<12:
                mm+=1
            elif mm==12:
                mm=1
                yy+=1
        MW[j+1]=[dd,"/",mm,"/",yy]
        n+=1
        j+=1

    i+=1
if w=="every week":
    a.date=MW
elif w=="every day":
    a.date=M

a.duration=input("enter the duration")
a.place=raw_input("enter the place")
a.description=raw_input("enter your the description of the event")

print T.__dict__
print a.__dict__
