#8.9

class Tgrade:
    def __init__ (grade):
        grade.deliverables=["0"]
        grade.project=0
        grade.TAE_BLOs=[0]*8
        grade.INF1_BLOs=[0]*8

class TprojectGrade:
    def __init__ (fin):
        fin.questionnaire=0.0
        fin.grades_reports=0.0
        fin.extension_exam=0.0

A=10
B=7.5
C=5
F=1
A=Tgrade ()
i=0
res=0
res1=0
res2=0
while i<len(A.deliverables):
    A.deliverables[i]=input('Enter your grade of Deriverable', i+1,':')
    i+=1
i=0
while i<len(A.deliverables):
    res=res+A.deliverables[i]
    i+=1

A.project=input("Enter your project mark")
i=0
while i<len(A.TAE_BLOs):
    A.TAE_BLOs[i]=input('Enter your TAE grade of BLO', i+1,':')
    res1=A.TAE_BLOs[i]+res1
    i+=1
i=0
while i<len(A.INF1_BLOs):
    A.INF1_BLOs[i]=input('Enter your INFO grade of BLO', i+1,':')
    res2=res2+A.INF1_BLOs[i]
    i+=1

B=TprojectGrade ()

B.questionnaire=input('Enter your questionnaire grade:')
B.grades_reports=input('Enter your grade report mark:')
B.extension_exam=input('Enter your extension exam grade:')

#Final Mark TAE


if res/8<0.8:

else:
    FINAL_MARK=(0.4*(res1/len(A.TAE_BLOs)))+0.4((B.questionnaire)*0.05+B.grades_reports*0.25+B.extension_exam*0.1))+0.1((res/(len(A.deliverables)))

FINAL_MARK=FINAL_MARK+(res1/8)+0.4 + (res/8)*0.1 + B.questionnaire*0.05+B.grades_reports*0.25+B.extension_exam*0.1

print ("TAE's final mark is,",FINAL_MARK)
